import sys
sys.path.append('/c/Users/nynto/Desktop/_Projects/Django/Project/myproject')
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'


BOT_NAME = 'myproject'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = .25
RANDOMIZE_DOWNLOAD_DELAY = True

ITEM_PIPELINES = {
    'myproject.pipelines.CkkImagesPipeline': 30,
    "myproject.pipelines.MongoPipeline": 300,
}
IMAGES_STORE = os.path.join(os.getcwd(),"HS")
# MONGO_URI = 
MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DATABASE = os.environ.get("MONGO_DATABASE")

 


