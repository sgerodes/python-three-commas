from dotenv import load_dotenv
load_dotenv()
import src.three_commas.api.ver1 as tc_api_ver1
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('urllib3.connectionpool').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

try:
    # logger.info(tc_api_ver1.bots.get_bot(bot_id=7745745))
    logger.info(tc_api_ver1.get_accounts())
except Exception as e:
    logger.exception('Exception occured')
