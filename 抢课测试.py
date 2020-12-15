# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:42:23 2020

@author: LiSunBowen
"""

import requests
import time

urlh = 'http://218.197.82.133/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=18020115'
url = urlh
# header 里面放自己登录之后的头信息，其中cookie相当于身份认证
header = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Connection': 'keep-alive', 'Content-Length': '606', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': 'JSESSIONID=EFDE1F7D64C', 'DNT': '1', 'Host': '218.197.82.133', 'Origin': 'http://218.197.82.133', 'Referer': 'http://218.197.82.133/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=18020115', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57', 'X-Requested-With': 'XMLHttpRequest'}

# header=dict([line.split(": ",1) for line in header[i].split("\n")]) 已弃用

# data 里面放抢课的data信息，这里放了全部网课的data信息，可以实现全部监控（丧心病狂）..
data = [
    {'jxb_ids': '6cd00fe3532d56581b5a36f4f5aeeb091e8bd0d46dad8ad2cd6b412244c516f3a9295f22094065ad041c8296f612140e47ca0a12cb77d0b90404f1ce6c09cb1dee375273e91f88f2b14511c6f8736cf41139923b2b952d90ea8b06aba2bf1ece1c59467bf2cbaba8a27f556d5eaeda9aa586f48ca79703d062ded9b2c617f086', 'kch_id': '8C341314ABA711E7E0530B50C5DADB8B', 'kcmc': '(TX9838)舌尖上的植物学(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '56b035ad5c4bcfd37eefcd51202732a6d31bfb477b3329b265ffa294684933a25cb19b8d1876499564a607dca88a49391d551d90e001a6a107cd43233192a1c413c330a659968a744bfd0c8c6fbd1d41909052567586da861c7d673018a8397297c20143430f125a416da5625eca97aeac67babe8eee0c340a6b57e312daaaf5', 'kch_id': 'TX3705', 'kcmc': '(TX3705)科学技术简史(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '7ceb1c515dfe4d0b4aa89ec0ec4ea17f55d0f6828d4eb4bd52dc48ae1a4325fb46fe3ad6427b42b76617fc14b88686044139d993d895561b351e8a1a7caddb58f04fdfec44ca944baa30f8edc9b7fa35faeb7c523a6b5bfa9fb2f49beeda854482baff914d439e75119e4fdc85baf552f240f8cfc52c964c49c5452fc17e9a0f', 'kch_id': '8C333E92ACE42D78E0530B50C5DA7285', 'kcmc': '(TX9839)创新中国(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '49e68e9053fa0162582cab4b17a67e6e8bd696df83605231be9c3e9bd2a7a46d7892f7d5db0c50e795b9aa8816c932263f9df0947340939c6722db07f26d579c79f68b192b0f6a1bff756540c2d8d9d30b50db6190ff8a4723c80e3f209d42e1a3ca774a45640d04ab764b493b54fea27c40ee33a75eb06b806bde85ced3c939', 'kch_id': '8C333E92ADFD2D78E0530B50C5DA7285', 'kcmc': '(TX9844)透过性别看世界(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '1ed93c0195240503dde46ba1ade71f01035e48dfac444b343bec6e7ea92a87ece377a6314dea94334fba360a93ea0d160db06c7b5ecf9159372486d70a4a0f037fb934b611bc540a098352d4b972db2e9b4559473a51b5474066a007723306e91a428df1cc504ac7c006394c12e3c6121d89e919e16c4087fe1bfbc2f63011de', 'kch_id': '8C3555B8B7F533A1E0530B50C5DA571C', 'kcmc': '(TX9841)欧洲文明的现代历程(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '2eebfdfd225602372e6a22035687895ba954580276265111d8c85326fd8e28fb54c7cfbda97797ea70ccb100d18a196a4b3f368da23870947597a19746ccef2e7fac6bcad3f03d40649e24a50588457e2b6cdebbfc32121dd291f5a6099a3e3d49a1ef138a2ff44accfde563a3d3e0a291cdaf8e91b3109cf1123a74546fb43b', 'kch_id': '8C3555B8B81733A1E0530B50C5DA571C', 'kcmc': '(TX9843)人生与人心(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '2a19fb0753a18f9a190f37b4ecdfcf2961fffb4631960a6e8fa88072e0e7c8e4b8706dd0453166618540a027d93c861435c76b166a48845e4feb31205a43a946286049d2c937ad268b0b0cab050485ab729d5d5608fb6e0536ba5ac29577d427ce8278296e401530835036317ef8fdd1eb3734c827c18a6c4f9d0f729525c2db', 'kch_id': '8C359F0300993A75E0530B50C5DA6F79', 'kcmc': '(TX9840)意义生活：符号学导论(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '363f54ce699f66cde8e0d495d0468221281737910107a9b57fe2578c515bbd9592ca4e4998e377175952abb95f50cc198fa7a2bee0b9cee51f41857f2f77ad04f6e25763d08773897c5e2e8b321b71fec25f2e1ebcb8232116f373b7740098dccad268d5eca955bd5669a4164d93e3d4998c0169c6c66576d4e0984685765218', 'kch_id': '8C35EFD84BF04408E0530B50C5DAF779', 'kcmc': '(TX9850)女性学：女性精神在现代社会中的挑战(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '63aa3a593993c55018775d9b77449b5eba87674f802f0c9368bb9887ae9d27e8fb945811c2454024ed377a1e4fa13f2841318f65f9b5b8be6c4fca00708a966b7e02b7279e46f3d5399119fff1204fbf11180e9cc1067e27df76dae30e2199608c12484d861b30d354c7880c9d9d4abfab76f6c688103d2b471f605725de4c48', 'kch_id': '8C35EFD90E2F43FCE0530B50C5DACDB5', 'kcmc': '(TX9848)中国古建筑欣赏与设计(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '634237ffeedc185e6a726fc2e767e71e6d2e0e1f15fc8fee1047d2d4d9254f084e6bd0575736067f1678e0f12e683a0ec076ca22a3298de430e811b6bd17d2dc0395ec8a20c74e592738b7ebbb69a7e0cb2d53970399c96687594da78adef9d2f376ef567e86c93c0fa08304829b8d4ee9a6bb430305669467bd517f7806e018', 'kch_id': '8C35EFD90FAE43FCE0530B50C5DACDB5', 'kcmc': '(TX9856)创业人生(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '0f3344e820d210d91dc36fef0cf12642bcd1ed8f162008c0179f7e39127c44780288b13481e04d8df32fc27a86482dc3f43b7ad339157d0cd98307311d37652fd56b80ba2d2c287179466e1d83ae8781613f9b1d9a8d51a2895c14126ff90dd279f1bab0526d3e5dd923cb22e02a015dee915272385d42810668fc7fd1c7d1ad', 'kch_id': '8C361735B7604840E0530B50C5DA62AB', 'kcmc': '(TX9853)人工智能(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '4868481ec1a7da2c64c334f884122d10f04b0eb40be2bd4ccc17ec5c1313350e014e861dae84b63ab851942929507dbd6f63750a5f5c059a81a0d40ff69c159f73d6299ec77c514bfbad8f3add20c807e3c8d84e773e65685e6497356140cd9effc8f7ac4b2d3eb5effb3af2e567861e961760eb95ebe44a06532d7338c1016b', 'kch_id': '8C3618DDE4D74898E0530B50C5DA3114', 'kcmc': '(TX9855)什么是科学(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '661351b52c256962b61bbe468177372367b909061bc4e7ccaeefda91aaaa30cdd0151ce641f9c9e07b92d4d695738c98151bf2de4284053ca7b69709d3c0a5098b3c336d982b6ce2b19ce67b48f7ad121f8f20d3705a3a6ad7da87de5c955788a1dd8e874bae4652a0898c0b85a7a2924919645cab84023155638721b207c21e', 'kch_id': '8C3618DF1263489CE0530B50C5DA039F', 'kcmc': '(TX9849)舞台人生：走进戏剧艺术(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '4c01da5abb2a894784a201a3ab31d3c87acfff258a19832cc4d973facef3aca6ec453ddb5a0bdf4a29c437fae8cf699a5e6ede671717dc0e38f711de1fda794c9206dbf2924c8a65b9f5c63f7d8f72dc6947a3ac5ed2531beb85c72728c0703edb98d6faa0e459a3dda8fc6e7501b4ddf9b7d30a7ea449ca6aac891b80993562', 'kch_id': '8C361A534B2148A8E0530B50C5DA4142', 'kcmc': '(TX9846)走进西方音乐(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '802ad1067ae7478146c2be304369ce907b80d4ceaeef2ab10c060b6a02786728b70a8b1639e2187965ffafdc6893fd43e3bdeb92f92b4d7104bc669280073b4e1c0463974048a9d7d7021f46d4326c522549e0c12774800ad54baa57aa1f928d4d0273797869a1295d56d5de923e3930827723375db4b40f2d2d92ec4b5407e0', 'kch_id': '8C361A534C1B48A8E0530B50C5DA4142', 'kcmc': '(TX9852)工程伦理(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '0797e86fdbf43183fca87ad498daac55ab80fe1cf28de9e62e7d2a533abe9b1550c90e5710cf451a696274d0ed69bcfcee68a86c8e90bb471039634ce56d105a8717120a0864e484a7c80da866e72eb32604794a2db3981e655d304eaec36ebfa4659b16f6ee1141efe1da4817fe88b0abc1c6c363245fa71c0bf97e5ed4ae28', 'kch_id': '8C3662B98FD55014E0530B50C5DA77A9', 'kcmc': '(TX9851)大学启示录：如何读大学(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '2e9ea2644ac420ad079f9a105fa7e1e7c880c50c88bf1b7e5ba2b826b3af9749f25e9cd66c484f4fa0e7f06d65cb906d4c59dd739d01e8ddc90a75fa0be759a134e93066ef6d591adec1a13edea6044bc60da638571e9a0d8da1656921a6a66641ad7555e84caf38ed0bfab8b1ea51cb5941aaa24bb4e1d685d8ddf0ffb665d3', 'kch_id': '8C3668AFE0F150CEE0530B50C5DAE7AD', 'kcmc': '(TX9857)大学生恋爱与性健康(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '766e4defd7398eb038bee17c9e275e0dfb5621439b69093099f6033b0fb7d4cc1f6603b9431667bd3cee8f488fb8593e1e481fc4a1ecd58fddb69a115b34f1233e1fc95ca861039a34749509d862f2b9663a1921b5595d0028d446adac8e97b30c13d737f0e146378d0fc870961e466a5f8e46246896ee9110ed37bcbea26650', 'kch_id': 'AEAC697A9F01DE46E0530B50C5DAC9E6', 'kcmc': '(TX9858)情商与智慧人生(网络通识课) - 1.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '30dad5cd1d08c11a936f61d5b8fc57b45755d7078af8f6fc5389025c5a4fc93533417af6d3bbb62469b025bc0c87ed38d26b16730981c2b46fa202aade06a145bb082b5c65938552dc814ef7e503686acfe794719f30b7c7c50c32ffc728b2c31295dab5a1f3ba5384b11fa7cb4f05aefb73c58a533592b353fd815552302c5c', 'kch_id': 'TX1001', 'kcmc': '(TX1001)当代中国经济(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '50e00edf0bebba22e9bb838a854a06cb015d18ead042b155bef5bed647b59e35c2dae0a5b73b3bcb5d60322c768d7b396c8a7a413ce73f0ead56ad040c5f67ea1d6bc78ea8c27c1fdeb5ddb86e94fe3c53d82f509a6856ec492babd23272ddbd669d071e3997630496eb22c71806da59020d69780fdb82ab1327386756a689d6', 'kch_id': 'TX1906', 'kcmc': '(TX1906)西方文化名著导读(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '794c473a01d1662eb4ef939eaf9dc27db1a1dc9090f7388f30d22c4fe11de4e2e80d4690f339817ae4eb2f81494fedb0f2d1ddaa22ff5c30f75f0d25a09ba0a532d4871628e2c9ad0eef169be7b646e54d4f05362716871c972495061b70cf1b6482b7813d631939e2cd0edfbb8da1bb593e8b7126f3f660b19477480c739273', 'kch_id': 'TX3707', 'kcmc': '(TX3707)西方哲学智慧(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '0da57b83ff43c7401b892dfaa1de6b07f8d0d9e5dc15d752e32dd6a23294d8d1646148626cb2cadc2d2bde01e0ce801b372d2991122b995ededb0ddde204be65519cf3cd02fbf163a86e2e03fd2bac193521b0293000b90fa4349f267adb0b284117fe34fa8c998e661f70fa4370fa4fa1daba83bebeedde6c76d2f7daa23819', 'kch_id': 'TX3708', 'kcmc': '(TX3708)先秦哲学(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '15d8bfe8d087c82ecb79a09fa32afef0b84c1daee3232fc534ddc033dab2cad7d22bb6cc84182f0d7503adf2150d1ac68fe10313aa94c3b3e168498703cfef31347158a3c9416ab9a753b40a38f076c9b77a17f65978ff9cfe3e7179a9293cc44501d4694fb0ccf276d273521c4978cbfdb18ff8f24e2c92a80d7fbe0d59f17b', 'kch_id': 'TX3713', 'kcmc': '(TX3713)追寻幸福：中国理论史视角(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'},
    {'jxb_ids': '3c764fddd682c8090b39c737f9642bcf799d17cecb5ef9cdd20697c36ee8b19927d493de46477c95908c4e4bb86ff4f055081857e5889fc0696ed95fe1f44b3eeec66d88d95e37cb1493a75f815530cf23c927771467584ef0b6581a875fd94867d69489c7152111a726fd38775f7365c1714084cc8ba7ba64e687994192908f', 'kch_id': 'TX4309', 'kcmc': '(TX4309)四大名著鉴赏(网络通识课) - 2.0 学分', 'rwlx': '2', 'rlkz': '0', 'rlzlkz': '1', 'sxbj': '1', 'xxkbj': '0', 'qz': '0', 'cxbj': '0', 'xkkz_id': 'B43BB9A6FD6296B9E0530B50C5DA7240', 'njdm_id': '2018', 'zyh_id': '0307', 'kklxdm': '10', 'xklc': '1', 'xkxnm': '2020', 'xkxqm': '12'}
    ]
# data[i]=dict([line.split(": ",1) for line in data.split("\n")]) 已弃用

t = -1  # 初始化t值，t是抢课后服务器返回值，返回-1表示因为满员或其他原因未抢课成功，返回1表示抢课成功
num = 0  # 计数器，记录重复发送了多少次
e = 0  # 记录出错次数，在后续代码中，出错14次就会停止执行程序并报错
p = 0  # 计算抢到的各个课程的学分和，避免超过学分上限，比如只需要3分，避免抢到5分
i = 0  # 初始化i=0，也可不写，因为在循环中i默认从0开始
p0 = int(input('请输入学分上限：'))  # 设置学分上限，比如输入4分，就不会抢到5分，但可能抢到3分停止
if isinstance(data, list):  # 判断data是不是列表，建议使用列表
    # 默认t=-1时才能进入循环体，现有学分P要小于设定的学分上限，错误次数e小于14次才能继续循环（可以调整），设置了num的上限，重复10000次后停止，避免无限循环，可以手动调整
    while (t == -1) and (p < p0) and (e < 5) and (num < 10000): # 出错5次停止
        for i in range(len(data)):
            try:
                if p + eval(data[i]['kcmc'].split(' ')[2]) <= p0:  # 获取data中的课程学分，避免抢到的学分超过上限
                    '''
                    发送请求，这是关键步骤
                    '''
                    t == -1
                    r = requests.post(
                        url, data=data[i], headers=header, timeout=5)

                    # 判断返回值，返回值的参数flag后是1或-1，代表选课成功、不成功
                    t = eval(eval(r.text)['flag'])
                    num = num+1  # 计数器
                    time.sleep(0.2)  # 每次提交请求后休息0.3秒（可以调整）
                    if t == -1:  # 返回-1抢课失败
                        print('没有抢到{}，重复执行第{}次,现学分{}'.format(
                            data[i]['kcmc'].split(' ')[0], num, p))
                    elif t == 1:  # 返回1抢课成功
                        p = p + eval(data[i]['kcmc'].split(' ')[2])  # 累加抢到的学分
                        print('>>抢课成功,课程名称:{}，现学分{}'.format(
                            data[i]['kcmc'], p))
                    if p == p0:  # 抢满学分时跳出循环，停止程序
                        break
                elif p + eval(data[i]['kcmc'].split(' ')[2]) > p0:  # 避免超过学分上限，若会超过，跳出循环，停止程序
                    print('-->当前已经抢到最大学分限度，现有学分{}'.format(p))
                    if p0 == 1:  # 学分上限是特殊情况，只需要抢到一分课即可跳出
                        t = 1
                    break
            except:  # 出现网络问题会提示以下信息
                print('\n***出现网络问题，请登入网站检查是否正常***')
                e = e + 1
    else:  # 不满足while的条件时显示以下内容
        if p + eval(data[i]['kcmc'].split(' ')[2]) > p0:  # 继续抢课会超过学分上限提示
            print('==已经抢到最大限度，现有学分{}=='.format(p))
        elif p == p0:  # 学分抢满提示
            print('==学分已经满，现学分{}=='.format(p))
        else:  # 其他问题提示
            print('出现其他问题')
else:  # 不是列表提示
    print('data不是列表，检查数据')
