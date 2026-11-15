# 数据来源与处理

核对日期：2026-11-15。

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
