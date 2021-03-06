##django_yaba, aka, django-yet-another-blog-application
###Dependencies:
    Django-tagging
    Python-Feedparser
    Python-Twitter
    Pillow
    six
###Demonstration:
You can see the blog in action at http://www.f4ntasmic.com. That version is a bit customized to my exact needs, but it's basically what you'll get when you use this applicaiton.

I know, we didn't have enough blog engines built with Django right? Hell, finding a name for this one was a PITA thanks to all the others ones that exists. Hence, YABA it is. If anyone else already has this, and I just missed it, let me know, and I'll change the name of this one. 

Purpose:
I tend to blog a bit (http://www.f4ntasmic.com), and have built my own blog previously using Django. I wanted something a bit more flexible though, so I decided to build it with the idea of being able to plug it anywhere with minimal configuration. I'm going to leverage YAML ( http://www.yaml.de/en/ ) for the theme of the blog, so that you can have a fairly pretty blog out of the box within minutes. Anyways, let me know if you have any questions.
###Features:

####Dynamic Themes:
   There are two "themes" (one is just an ugly hack of the default, intended for test purposes not for actual use) now usable via the Admin UI. The default site configuration is loading from a fixture on initial syncdb, which sets up the initial themes. Obviously that means it's possible to create a theme, put it in the appropriate theme folder, and then create a theme in the Admin panel. You just have to name it the same as your directory in the themes path. Obviously, following my directory structure in the themes will lead to best results.

####WYSIWG Editor:
   Using TinyMCE
   Works

####Blog Posts:
   Will allow previews for authenticated users eventually. Backburner.
####RSS Feed:
   They appear to work properly now.. Doesn't work in staging, but it does work on www.f4ntasmic.com for some reason. Same code, different results. I'd try to wrap my head around it, but I fear I'd only hate myself for it.
####BlogRoll:
   Quite functional. One would hope right? They're flipping links.
####Articles:
   The articles are items that won't show up in the traditional main news feed. Also, if you check the "Buttoned" box, then the article will have a link to it on the top main nav bar. Currently functional
####Comments:
   If you want to use comments, set DJANGO_COMMENTS=True in your settings file.
####Social Media:
   Currently can grab your latest tweets, GitHub commits, and builds links to submit stories to Digg, Reddit, Delicious, and StumbleUpon. Github/Twitter configurable via simple settings in settings.py. If you don't want to display your tweets or github commits, just leave those fields empty in settings.py. If those are blank, you'll never see them again. 
####Search:
   You can now search for stories based on title/body contents. It's not super advanced, but it's functional.
####Galleries:
   You can now add new photo galleries to your site. I've placed a link to the gallery list on the top nav bar for easy browsing of galleries as well. It auto creates thumbnails and links to the full size of the image as well. So far works pretty well, but isn't extensively tested at this time.
###Installation Instruction:
   There are two ways to install yaba,
   1. You can easy_install it, and make use of it in your project of choice
   as a blog. Currently it's not incredibly well tested as a pluggable, so your mileage may vary. If you do use it and
    run into problems PLEASE let me know by submitting an issue or emailing me. I'd love to help resolve any issues you
    run into. So right now you can just 'easy_install django-yaba' to install this package.

   2. If you don't want to use easy_install, another way to install this app is to copy the project path and paste it into your virtualenv easy_install path.
   Paste this project path into
   /path/to/your/virtualenv/pythonx.x/site-packages/easy_install.pth

   Then you'll need to put the following variables in your settings.py:
<pre><code>
    ###############################################
    # django-yaba specific settings below         #
    ###############################################
    # GitHub UserName for sidebar GitHub List - Leave blank if you don't want to use it
    GITHUB_USERNAME = 'GITHUB_USER_HOLDER'

    # Twitter UserName for sidebar Twitter List and Automatic Tweets
    TWITTER_USERNAME = 'TWITTER_USER_HOLDER'
    TWITTER_PASSWORD = "TWITTER_PASS_HOLDER"

    # Blog Name
    BLOG_NAME = 'SITE_NAME_HOLDER'

    # Blog URL
    ROOT_BLOG_URL = 'http://URL_HOLDER/'

    # Root system path
    PROJECT_DIR = os.path.dirname(__file__)

    # Disqus Settings
    DISQUS_API_KEY = "DISQUS_API_HOLDER"
    DISQUS_WEBSITE_SHORTNAME = "DISQUS_SHORT_HOLDER"

    # If you want to use contrib.comments set the following to True
    DJANGO_COMMENTS = False

    SITE_ID = 1
    ################################################
</code></pre>
   Then you'll want to add the following applications to your INSTALLED_APPS:
<pre><code>
    'django.contrib.comments', #optional
    'django.contrib.sites',
    'tagging',
    'django_yaba',
    'django',
</code></pre>
   And run
<pre><code>
    ./manage.py syncdb
</code></pre>
   Finally YaBa does have it's own theming that it uses, so I've included in the package all the media that I use on
   www.f4ntasmic.com. You'll need to put that in your media path if you want to make use of it. Enjoy!
