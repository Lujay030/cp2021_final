from bs4 import BeautifulSoup

# ref: https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
# ref: https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings

'''
設法讀出各班各組學員學號資料
'''
repo_path = "Y:/tmp/cp2021_final"
class_name = "1a"
group_file = repo_path + "/downloads/" + class_name + "_grouping.txt"

with open(group_file, encoding="utf-8") as f:
    data = f.read().splitlines()
data = list(filter(None, data))
#print(data)
grp_count = 0
grp_title = []
grp_mem = []
grp_big = []
for i in data:
    if class_name in i:
        mem_count = 0
        grp_count += 1
        grp = i
        # 納入各組組序標題
        grp_title.append(i)
        # 若 grp_mem 有值, 表示已經讀完各組學員名單
        # 就可以將該組全員名單納入 grp_big 數列中
        # 然後 grp_mem 重新設為空數列, 準備納入下一組員名單
        if len(grp_mem) > 1:
            grp_big.append(grp_mem)
            grp_mem = []
        #print("組別:", grp_count, grp)
    else:
        # 讀完各組組序標題後, 將逐一將組員名單納入 grp_mem 數列中
        grp_mem.append(i)
        mem_count += 1
        student_id = i
        #print("學員:", mem_count, student_id)
# 離開組序標題後, 必須納入最後一組學員名單
grp_big.append(grp_mem)
# 查驗是否正確讀入各班組員名單
#print(grp_title, grp_big)
for i in range(len(grp_title)):
    print(grp_title[i], grp_big[i])

'''
根據學號, 從 downloads 目錄取出該學員的期末報告網頁 
'''
'''
html_location = repo_path + "/downloads/" + student_id + "_html.txt"
with open(html_location, encoding="utf-8") as f:
    student_html = f.read()

#print(student_html)

# 動態網頁檔案所在路徑
file_location = repo_path + "/config/content.htm"
# 將動態網頁檔案內容讀出, 存入 data 變數區
with open(file_location, encoding="utf-8") as f:
    data = f.read()

#print(data)

# 利用 data 建立 soup
soup = BeautifulSoup(data, "lxml")
# 利用 student_html 建立 soup
soup2 = BeautifulSoup(student_html, 'lxml')
# 插入的 student_html 會多出 <html><body></body></html>
# 最後存檔前必須移除
for i in soup.find_all('h2'):
    if i.text == "1ag1":
        # 取 soup2 中的 tag
        for j in soup2:
        # 在 soup 中對應 <h2>1ag1</h2> tag 之後插入 j tag
            i.insert_after(j)

output = str(soup)
output = output.replace("<html><body", "")
output = output.replace("</body></html>", "")
print(output)
'''


