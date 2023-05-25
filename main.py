from import_data import DataImport

path="/Users/User/Desktop/STEM2-DashboardV3/data/"


di=DataImport( "implications.db")
di.create_tables()
di.import_txt(path)




