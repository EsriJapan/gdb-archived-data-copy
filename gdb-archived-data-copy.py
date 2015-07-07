# coding:utf-8

"""-------------------------------------------------------------------------------
 Name:        gdb_archived_data_copy.py
 Purpose:     export shapefile data from selectied time in geodatabase

 Author:      mnatsume

 Created:     10/06/2015
-------------------------------------------------------------------------------
"""

import sys
import arcpy
import os.path

def main(argv):
    """
    使い方: python gdb_archived_data_copy.py 出力先ディレクトリ DBPLATFORM(POSTGRESQL/SQLSERVER/ORACLE) DBインスタンス 認証方法(DATABASE_AUTH/OPERATING_SYSTEM_ATH) ユーザー名 パスワード データベース名 フィーチャクラス名 日付(yyyy-MM-dd HH:mm:ss)
    """

    # allow overwrite
    arcpy.env.overwriteOutput = True

    tmp_file = "tmp.sde"

    (out_dir, database_platform, instance,
    auth, user, passwd, database, fc_name, date) = argv[1:]

    # create database connection


    try:
        arcpy.CreateDatabaseConnection_management(out_dir, tmp_file, database_platform, instance,
                                                    auth, user, passwd, "SAVE_USERNAME",
                                                    database, "#", "POINT_IN_TIME", "#", date)
    except Exception as e:
        print arcpy.GetMessages()

    # copy

    # join function to get path for specific feature class in geodatabase
    copy_fc = reduce(os.path.join, (out_dir, tmp_file, fc_name))

    # saving place for .shp, which is same as where you created database connection
    # Process:(Feature Class To Shapefile (multiple))
    # this time I use only (single)
    try:
        arcpy.FeatureClassToShapefile_conversion(copy_fc, out_dir)
    except Exception as e:
        print arcpy.GetMessages()


if __name__ == '__main__':
    main(sys.argv)
