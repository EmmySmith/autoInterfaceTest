# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 4:59 PM
# @Author  : Emmy
# @File    : a_material.py
import  unittest
from  common.public import *
from common.commonData import *

class a_material(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path1 = "/api/icem-component/material/groups?type=image&appid=2019090466884677"
        self.path2 = "/api/icem-component/material/save?appid=2019090466884677"
        self.path3 = "/api/icem-component/material/find?type=image&groupId=0&title=&page=0&size=20&appid=2019090466884677"
        self.path4 = "/api/icem-component/material/delete?id=450&appid=2019090466884677"

    def test_a0_savemicropage(self):
        """获取分组"""
        self.url = self.host + self.path1
        data = {
        }
        print(self.url)
        response = requests.get(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        commonData.groupId = json.loads(response.text)["body"][0]["id"]
        print("分组ID为:" + str(commonData.groupId))
        assert response.json()['error'] == 0

    def test_a1_savemicropage(self):
        """上传图片"""
        self.url = self.host + self.path2
        data = {
            "type": "image",
            "title": "8339340_144203764154_2.jpg",
            "group_id":commonData.groupId,
            "url": "https://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/4e24bbeb190f436fb60a0eecb35742c1.jpg"
            }
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0

    def test_a2_savemicropage(self):
        """获取上传图片"""
        self.url = self.host + self.path3
        data = {
        }

        print(self.url)
        response = requests.get(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.imageId = json.loads(response.text)["body"]["content"][3]["id"]
        print("图片id为：" + str(commonData.imageId))
        assert response.json()['error'] == 0

    def test_a3_savemicropage(self):
        """删除图片"""
        self.url = self.host + self.path4
        data = {
        }

        print(self.url)
        response = requests.delete(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(a_material())
