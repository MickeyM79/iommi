from iommi import *
from iommi.admin import Admin
from django.urls import (
    include,
    path,
)
from django.db import models
from tests.helpers import req, user_req, staff_req
from docs.models import *
request = req('get')

from tests.helpers import req, user_req, staff_req
from django.template import Template
from tri_declarative import Namespace
from iommi.attrs import render_attrs
from django.http import HttpResponseRedirect
from datetime import date
import pytest
pytestmark = pytest.mark.django_db




def test_parts__pages():
    # language=rst
    """
    Parts & Pages
    -------------

    """
    

def test_how_do_i_override_part_of_a_part_page():
    # language=rst
    """
    How do I override part of a part/page?
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This is all just *standard* tri.declarative magic. But as you are likely new to it
    this might take a while to get used to. Let's say you created yourself a master template
    for your site.


    """
    class BasePage(Page):
        title = html.h1('My awesome webpage')
        subtitle = html.h2('It rocks')

    # language=rst
    """
    Which you can use like this:


    """
    def index(request):
        class IndexPage(BasePage):
            body = ...
        return IndexPage(parts__subtitle__children__text='Still rocking...')

    # @test

    index(req('get'))

    # language=rst
    """
    Here you can see that `Part` s (`Page` s are themselves `Part` s) form a tree and the direct children are gathered in the `parts` namespace. Here we overwrote a leaf of
    an existing namespace, but you can also add new elements or replace bigger
    parts (and most of the time it doesn't matter if you use the class Member or the
    keyword arguments to init syntax):


    """
    def index(request):
        class IndexPage(BasePage):
            title = html.img(attrs=dict(src='...', alt='...'))
        return IndexPage(parts__subtitle=None)

    # @test

    index(req('get'))

    # language=rst
    """
    In the above we replaced the title and removed the subtitle element completely. The
    latter of which shows one of the gotchas as only `str`, `Part` and the django
    template types are gathered into the parts structure when a `Part` class definition
    is processed. As `None` is not an instance of those types, you can remove things
    by setting their value to `None`.

    .. _Page.title:

    """
    

def test_how_do_i_set_the_title_of_my_page():
    # language=rst
    """
    How do I set the title of my page?
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    As in the text shown in the browser status bar?


    """
    Page(title='The title in the browser')

    # language=rst
    """
    Note that this is different from


    """
    class MyPage(Page):
        title = html.h1('A header element in the dom')
    MyPage()

    # language=rst
    """
    Which is equivalent to:


    """
    Page(parts__title=html.h1('A header element in the dom'))


    # language=rst
    """
    .. _Page.context:

    """
    

def test_how_do_i_specify_the_context_used_when_a_template_is_rendered():
    # language=rst
    """
    How do I specify the context used when a Template is rendered?
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    """
    def index(request):
        context = {'today' : date.today()}
        class MyPage(Page):
            body = Template("""A django template was rendered on {{today}}.""")
        return MyPage(context=context)

    # @test

    index(req('get'))

    # language=rst
    """
    You can use the full power of `tri.declarative` to construct the context. This
    not only makes the above shorter, but also makes it easy to write abstractions that
    can be extended later:


    """
    Page(
        parts__body=Template("""A django template was rendered on {{today}}."""),
        context__today=date.today(),
    )
