# encoding: utf-8

"""
@version: 
@author: liriqiang
@file: api.py
@time: 16-6-2 下午7:03
"""

import os, sys, time, re
from Crypto.Cipher import AES
import crypt
import pwd
from binascii import b2a_hex, a2b_hex
import hashlib
import datetime
import random
import subprocess
import uuid
import json
import logging
import urllib
import urllib2

from settings import *
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response, RequestContext
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test


def set_log(level, filename='opsplatform.log'):
    """
    return a log file object
    根据提示设置log打印
    """
    log_file = os.path.join(LOG_DIR, filename)
    if not os.path.isfile(log_file):
        os.mknod(log_file)
        os.chmod(log_file, 0777)
    log_level_total = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARN, 'error': logging.ERROR,
                       'critical': logging.CRITICAL}
    logger_f = logging.getLogger('opsplatform')
    logger_f.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file)
    fh.setLevel(log_level_total.get(level, logging.DEBUG))
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger_f.addHandler(fh)
    return logger_f


def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    return subprocess.call(cmd, shell=True)


def chown(path, user, group=''):
    if not group:
        group = user
    try:
        uid = pwd.getpwnam(user).pw_uid
        gid = pwd.getpwnam(group).pw_gid
        os.chown(path, uid, gid)
    except KeyError:
        pass


def mkdir(dir_name, username='', mode=755):
    """
    insure the dir exist and mode ok
    目录存在，如果不存在就建立，并且权限正确
    """
    cmd = '[ ! -d %s ] && mkdir -p %s && chmod %s %s' % (dir_name, dir_name, mode, dir_name)
    bash(cmd)
    if username:
        chown(dir_name, username)


def list_drop_str(a_list, a_str):
    for i in a_list:
        if i == a_str:
            a_list.remove(a_str)
    return a_list


def http_success(request, msg):
    message = msg
    return render_to_response('success.html', locals(), RequestContext(request))


def http_error(request, msg):
    message = msg
    return render_to_response('error.html', locals(), RequestContext(request))


def get_object(model, **kwargs):
    """
    use this function for query
    使用改封装函数查询数据库
    """
    for value in kwargs.values():
        if not value:
            return None

    the_object = model.objects.filter(**kwargs)
    if len(the_object) == 1:
        the_object = the_object[0]
    else:
        the_object = None
    return the_object


def page_list_return(total, current=1):
    """
    page
    分页，返回本次分页的最小页数到最大页数列表
    """
    min_page = current - 2 if current - 4 > 0 else 1
    max_page = min_page + 4 if min_page + 4 < total else total

    return range(min_page, max_page + 1)


def pages(post_objects, request):
    """
    page public function , return page's object tuple
    分页公用函数，返回分页的对象元组
    """
    paginator = Paginator(post_objects, 20)
    try:
        current_page = int(request.GET.get('page', '1'))
    except ValueError:
        current_page = 1

    page_range = page_list_return(len(paginator.page_range), current_page)

    try:
        page_objects = paginator.page(current_page)
    except (EmptyPage, InvalidPage):
        page_objects = paginator.page(paginator.num_pages)

    if current_page >= 5:
        show_first = 1
    else:
        show_first = 0

    if current_page <= (len(paginator.page_range) - 3):
        show_end = 1
    else:
        show_end = 0

    # 所有对象， 分页器， 本页对象， 所有页码， 本页页码，是否显示第一页，是否显示最后一页
    return post_objects, paginator, page_objects, page_range, current_page, show_first, show_end


class PyCrypt(object):
    """
    This class used to encrypt and decrypt password.
    加密类
    """

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    @staticmethod
    def gen_rand_pass(length=16, especial=False):
        """
        random password
        随机生成密码
        """
        salt_key = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        symbol = '!@$%^&*()_'
        salt_list = []
        if especial:
            for i in range(length - 4):
                salt_list.append(random.choice(salt_key))
            for i in range(4):
                salt_list.append(random.choice(symbol))
        else:
            for i in range(length):
                salt_list.append(random.choice(salt_key))
        salt = ''.join(salt_list)
        return salt

    @staticmethod
    def md5_crypt(string):
        """
        md5 encrypt method
        md5非对称加密方法
        """
        return hashlib.new("md5", string).hexdigest()

    @staticmethod
    def gen_sha512(salt, password):
        """
        generate sha512 format password
        生成sha512加密密码
        """
        return crypt.crypt(password, '$6$%s$' % salt)

    def encrypt(self, passwd=None, length=32):
        """
        encrypt gen password
        对称加密之加密生成密码
        """
        if not passwd:
            passwd = self.gen_rand_pass()

        cryptor = AES.new(self.key, self.mode, b'8122ca7d906ad5e1')
        try:
            count = len(passwd)
        except TypeError:
            raise ServerError('Encrypt password error, TYpe error.')

        add = (length - (count % length))
        passwd += ('\0' * add)
        cipher_text = cryptor.encrypt(passwd)
        return b2a_hex(cipher_text)

    def decrypt(self, text):
        """
        decrypt pass base the same key
        对称加密之解密，同一个加密随机数
        """
        cryptor = AES.new(self.key, self.mode, b'8122ca7d906ad5e1')
        try:
            plain_text = cryptor.decrypt(a2b_hex(text))
        except TypeError:
            raise ServerError('Decrypt password error, TYpe error.')
        return plain_text.rstrip('\0')


class ServerError(Exception):
    """
    self define exception
    自定义异常
    """
    pass


class JsonResponse(HttpResponse):
    """
    An HTTP response class that consumes data to be serialized to JSON.

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before EcmaScript 5. See
      the ``safe`` parameter for more information.
    :param encoder: Should be an json encoder class. Defaults to
      ``django.core.serializers.json.DjangoJSONEncoder``.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``.
    """

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder)
        super(JsonResponse, self).__init__(content=data, **kwargs)


def defend_attack(func):
    def _deco(request, *args, **kwargs):
        if int(request.session.get('visit', 1)) > 100:
            logger.debug('请求次数: %s' % request.session.get('visit', 1))
            return HttpResponse('Forbidden', status=403)
        request.session['visit'] = request.session.get('visit', 1) + 1
        request.session.set_expiry(300)
        return func(request, *args, **kwargs)
    return _deco


def require_permission(perm):
    """
    要求用户是某种权限的装饰器
    """

    def _deco(func):
        def __deco(request, *args, **kwargs):
            request.session['pre_url'] = request.path
            if not request.user.is_authenticated():
                return HttpResponseRedirect(reverse('login'))
            if not request.user.has_perm(perm):
                return HttpResponseRedirect(reverse('index'))
            return func(request, *args, **kwargs)

        return __deco

    return _deco


def get_role_key(user, role):
    """
    由于role的key的权限是所有人可以读的， ansible执行命令等要求为600，所以拷贝一份到特殊目录
    :param user:
    :param role:
    :return: self key path
    """
    user_role_key_dir = os.path.join(KEY_DIR, 'user')
    user_role_key_path = os.path.join(user_role_key_dir, '%s_%s.pem' % (user.username, role.name))
    mkdir(user_role_key_dir, mode=777)
    if not os.path.isfile(user_role_key_path):
        with open(os.path.join(role.key_path, 'id_rsa')) as fk:
            with open(user_role_key_path, 'w') as fu:
                fu.write(fk.read())
        logger.debug(u"创建新的系统用户key %s, Owner: %s" % (user_role_key_path, user.username))
        chown(user_role_key_path, user.username)
        os.chmod(user_role_key_path, 0600)
    return user_role_key_path


def get_tmp_dir():
    seed = uuid.uuid4().hex[:4]
    dir_name = os.path.join('/tmp', '%s-%s' % (datetime.datetime.now().strftime('%Y%m%d-%H%M%S'), seed))
    mkdir(dir_name, mode=777)
    return dir_name


def api_call(url, param={}, method='GET', headers={}):
    '''
    get data from other system via api
    '''
    if isinstance(param, dict):
        param = urllib.urlencode(param)
    try:
        if method == 'GET':
            req = urllib2.Request('%s?%s' % (url, param), headers=headers)
        else:
            req = urllib2.Request(url, param, headers)
        r = urllib2.urlopen(req).read()
        return json.loads(r)
    except Exception, e:
        return {'msg': e, 'code': -1}


CRYPTOR = PyCrypt(KEY)
logger = set_log(LOG_LEVEL)
