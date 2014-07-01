from django import template
from django.db.models import get_model
Story = get_model("django_yaba", "Story")

register = template.Library()

class BlogPostNode(template.Node):
    def __init__(self, post_count):
        self.post_count = int(post_count)

    def render(self, context):
        blog_posts = Story.objects.all().order_by('-created')
        if blog_posts.count() > self.post_count:
            blog_posts = blog_posts[:self.post_count]
        context.update({'blog_posts': blog_posts})
        return ''

@register.tag
def get_blog_posts(parser, token):
    """
    Usage:
    {% get_blog_posts "3" %}
    {% if blog_posts %}
    {% for post in blog_posts %}
    <h1> {{ post.title }} </h1>
    {% endfor %}
    {% endif %}
    """

    bits = token.contents.split()
    count = bits[1]
    count = count[1:-1]
    if len(bits) != 2:
        raise TemplateSyntaxError, "get_blog_posts requires 1 argument"
    return BlogPostNode(count)
