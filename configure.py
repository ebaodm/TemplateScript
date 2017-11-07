# 生成控制文件的配置说明
sqlloader_configure = {"file_name_ext":"txt", "terminated_by":",", "enclosed_by":'"', "append_type":"replace", "nls_lang":"AMERICAN_AMERICA.ZHS16GBK"}

# real_data_type 生成创建中间表的控制选项, 真实的数据类型或者实际定义的数据类型,
# table_prefix 创建表时加的前缀，为了支持一些项目需要加一个表名前缀
create_table_configure = {"real_data_type": False, "table_prefix":""}

