# -*- coding: utf-8 -*-

import pdfplumber
import sys
import os


def print_pdf(pdf_path):
    if pdf_path[-3:] != 'pdf':
        return
    print('正在提取pdf：[%s]' % (pdf_path))
    pdf = pdfplumber.open(pdf_path)

    line_id = 1
    for page in pdf.pages:
        # 获取当前页面的全部文本信息，包括表格中的文字
        text = page.extract_text()
        lines = text.split('\n')
        for line in lines:
            if 'Balance' in line and 'Today' in line:
                print('第%d行：%s' % (line_id, line))
            line_id += 1

        # for table in page.extract_tables():
        #     # print(table)
        #     for row in table:
        #         print(row)
        #     print('---------- 分割线 ----------')

    pdf.close()


def print_pdfs_in_one_folder(root_path):
    print('正在检查文件夹：[%s] (注：只保留 Balance Today行)' % (root_path))
    g = os.walk(root_path)

    for path, dir_list, file_list in g:
        for file_name in file_list:
            pdf_file = os.path.join(path, file_name)
            print_pdf(pdf_file)


if __name__ == '__main__':
    folder_path = sys.argv[1]
    print_pdfs_in_one_folder(folder_path)
