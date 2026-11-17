# 数据来源与处理

核对日期：2026-11-16。

## 地理底图与地点

- © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)，数据库按ODbL提供。道路、铁路、海岸线、湿地、城镇、部分景点坐标由公开Overpass接口获取。
- [Natural Earth 1:10m land](https://www.naturalearthdata.com/about/terms-of-use/)，公有领域，用于区域陆地填充；小岛补充使用OSM闭合海岸线。
- 个别地点采用沙巴旅游局、运营商、Waze、Mapcarta、Wikimedia及其他地图资料；每个地点的详情均有对应位置来源链接。

已处理地理数据是上述公开数据的裁剪、降精度与简化版本；原有许可和署名要求继续适用。

## 海拔与地形着色

- [Mapzen / AWS Terrain Tiles](https://registry.opendata.aws/terrain-tiles/)，[Terrarium编码说明](https://github.com/tilezen/joerd/blob/master/docs/formats.md)。
- SRTM and GMTED2010 terrain data courtesy of the U.S. Geological Survey. Global ETOPO1 terrain data courtesy of NOAA. 完整[来源署名与许可](https://github.com/tilezen/joerd/blob/master/docs/attribution.md)。
- 取115–119.2°E、4–7.2°N，缩放级别9，共42个公开瓦片。按官方公式解码到米，轻度平滑并以每3像元取样，再提取200、1000、2500米分层多边形，简化到约百米尺度。处理会降低局部细节；绝不用于实地导航或判断安全坡度。
- 高程分层只是地貌理解辅助，不等同于土地利用、植被或严格地貌类型。湿地另外使用OSM标注边界；未测绘区域不作外推。

## 交通时间

主要依据沙巴旅游局、Sabah Parks、铁路局、机场／航空公司及当地运营商公开路线资料，并加入保守的市区交通估算。每个地点详情附来源；未获实时路线支持的市区车程、步行时间和新增城镇车程明确作为规划估算。

## 软件

[D3 7.9.0](https://github.com/d3/d3) 按ISC许可证提供。地图展示使用d3-geo进行真实经纬度投影。网页导出层提供独立运行样式和本地展示状态，不使用用户账号数据或密钥。

## 市区详图（2026-11-16新增）

36处景点／交通参考点，按市中心、里卡士与沙巴大学、丹绒亚路与南部分区。城市道路、公园、沙滩与UMS校园边界来自OSM API 0.6地图摘录；派生数据库按ODbL提供。区域边界是已测绘范围，不代表全部设施开放；无完整边界的区域不补画虚构范围。坐标来源逐点附在网页详情中。车程、步行时间为加雅街出发的规划估算。

- [沙巴旅游局：水上清真寺](https://sabahtourism.com/destination/city-mosque/)：页面列周五关闭参观，其他日分时开放、需登记和遵守着装。圣诞假期临时安排未确认。
- [沙巴旅游局：加雅街周末市场](https://sabahtourism.com/article/gaya-street-the-sensational-weekend-street/)：周五、周六Api-Api夜市通常18:00–午夜；周日早市在同一街区。菲律宾手工艺市场、滨海熟食夜市、中央市场是另一片滨海市场群，图中分别标点。
- [UMS官方网站](https://www.ums.edu.my/v5/)、[UMS可持续发展介绍](https://strategi.ums.edu.my/sustainability/sdg11.html)：校园、清真寺和ODEC海滩。图钉分别表示校区中心、清真寺和海滩，不将到校门的时间误作到校内景点的时间。具体游客入校安排须再核对。
- [Signal Hill运营方游客说明](https://signalhill.my/visitor-information)：目前观景台关闭；步道与钟楼开放安排另列。不可因步道可走而推断观景台能入内。
- [沙巴博物馆官方公告](https://museum.sabah.gov.my/updates)：仍列有主楼展厅关闭公告；地图保留博物馆园区，提醒出行前核对实际开放设施。

## 12月24–29日行程图

- 日期与产品时段来自11月17日更新的计划。Papar中午场11:00–15:00，早场09:00–13:30暂按村内时段。若含接送，须改用订单的到村、离村时间，避免重复计时。其余分段停留为规划预算。
- 驾车几何取自[OSRM公开服务](https://project-osrm.org/)，底层路网为OSM；对几何降采样，标注参考里程。OSRM自由流车速不用于旅游车程；保留山路、接送与天气余量。个别反向短程沿用道路走廊并注明，不能用于逐向导航。
- 海上直线与城市步行连线为方向示意，非实际航迹／步行道路。Weston图钉为活动区域，未虚构运营商码头及河上航线。
- [JSK官方码头说明](https://www.jskmantananiresorts.my/faq)及其[地图位置](https://maps.app.goo.gl/r57MyYMo6TZcRjxf9)：仅用于Rampayan方向示例，**没有据此认定用户的懒猫小美人鱼产品使用JSK码头／度假村**。具体岛屿、营地、集合码头仍需订单确认。
- [懒猫美人鱼岛常规线路](https://www.lanmao.cn/blog/mantanani-island-day-tour-booking/)提到Kuala Abai。[另一小美人鱼产品](https://www.travelboxsabah.com/zh/product/the-one-mantanani)使用Rampayan，两者仅用于估算。[小美人鱼岛位置](https://www.geonames.org/1736451/pulau-mantanani-kecil.html)用于标岛屿方向。
- [大王花与Weston组合产品示例](https://huodong.ctrip.com/ottd-activity/dest/t95701283.html)说明市场上有同日组合，12月27日的库存与懒猫交接尚未确认。[Weston当地图示时刻](https://www.borneotravelnetwork.com/tour-packages-sabah-bki06-western-eco-tour.php)用于估计岸上、乘船、晚餐及回程用时。
- [亚庇12月日照表](https://www.timeanddate.com/sun/malaysia/kota-kinabalu?month=12&year=2026)给出12月26日日落约18:09，当日能见度取决于天气。
- [Borneo Eco Tours步道说明](https://www.borneoecotours.com/blog/5-trails-to-explore-in-kinabalu-national-park/)分别列Kiau View为2344米、约1小时，Silau-Silau为3396米、约1–1.5小时。游览预算另留衔接和休息。
- [铁路局日落列车](https://railway.sabah.gov.my/pelancongan/ttmsb/)：通常周六16:00–20:00，丹绒亚路至Benoni方向往返，非闭合环线。只显示已测绘铁路走廊，河口末端接驳待运营方确认。**2026-12-26开行尚未确认。**
- [Papar的Borneo Cultural Village](https://sabahtourism.com/destination/borneo-cultural-village-2/)：用户已确认这家文化村，不能与Mari Mari混用。
- [大王花信息中心](https://sabahtourism.com/destination/rafflesia-information-centre/)：Tambunan基地；花期与林中找花时间不固定。调整后改在周日07:00–13:30参观，同日Weston团13:00接人，两段相差30分钟且没有交接余量。
- [小红书：神山公园徒步实录](https://www.xiaohongshu.com/explore/6a6eedac000000003300989b)：已阅读正文与作者步道图；作者原计划KVT＋SST，实际因雨和泥泞改短线。徒步与登顶、观光包车不同。仅提炼规划经验，不复刻图片、全文或个人价格。
- [小红书：AMT旅行社神山包车观光](https://www.xiaohongshu.com/explore/6a7ff5ea0000000005033f55)：旅行社账号的观景点、市场、温泉鱼疗、奶牛场一日安排，17:00是开始回城，不是抵达。不是KVT＋SST徒步产品，不能直接相加。
- KVT/SST几何来自OSM已测绘路径（包括ways 77931739、77931740、77931741等）；地图与运营商统计长度不同，约5–6公里、2.5–3.5小时为规划值，雨后可能更久。未把缺失连接伪造成完整GPS环线；当天以公园地图及开放情况为准。

D3库已嵌入页面，许可证保留在源码vendor/D3-LICENSE；地图显示不依赖第三方地图瓦片或运行时CDN请求。详情中的外链仍需要网络。
