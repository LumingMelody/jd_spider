from openpyxl import Workbook

from service.model.mysql_models import JD_CATEGORY


# wb = Workbook()
# ws = wb.active
# ws.append(['商品ID', '类目'])


def save_category(info):
    jd_category = JD_CATEGORY()
    jd_category.sku = info['sku']
    jd_category.category = info['category']
    jd_category.save(force_insert=True)
    # shop_name = info['shop_name']
    # goods_id = info['goods_id']
    # icon = info['icon']
    # detail_url = info['detail_url']
    # all_comment = info['all_comment']
    # video_show = info['videocount']
    # good_comment = info['goodcount']
    # general_comment = info['generalcount']
    # poor_comment = info['poorcount']
    # after_comment = info['aftercount']
    # good_score = info['goodrate']
