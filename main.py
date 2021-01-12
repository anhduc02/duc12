#các thư viện cần thiết
import folder_op, web_op






def start():
    url_list = ['htpps':'vietnamnet.vn'] #chứa các đường link được duyệt
    history = [] #chứa các đường link được duyệt
    max_page = 1000 #quy định số lượng trang web tải về
    data_folder = "C: \\Users\\MyPC\\Dowloads\\Crawl\\"


#kịch bản tải các trang web
while (could < maxpage) and (len(url_list > 0)):
    url = url_list.pop(0)
    page = web_op.doc_noi_ dung(url)
    link =web_op.lay_cac_duong_link(page)
    for item in link : # duyệt các đường link để kiểm tra tính hợp lệ
        if web_op

