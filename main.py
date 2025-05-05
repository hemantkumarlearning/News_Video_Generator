from scraper import trending_news
from script_generator import generate_script_with_llama
from video_creater import create_video

headlines = trending_news()
script = generate_script_with_llama(headlines)
create_video(script)