# python_format_sql.py
import jpype

def format_sql(file_path, db_vendor):
    # Start the Java Virtual Machine (JVM)
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", f"-Djava.class.path=C:\\prg\\gsp_demo_java\\lib\\gudusoft.gsqlparser-2.7.1.6.jar")

    try:
        # Import the necessary Java classes
        TGSqlParser = jpype.JClass("gudusoft.gsqlparser.TGSqlParser")
        GFmtOptFactory = jpype.JClass("gudusoft.gsqlparser.pp.para.GFmtOptFactory")
        FormatterFactory = jpype.JClass("gudusoft.gsqlparser.pp.stmtformatter.FormatterFactory")
        
        # Load EDbVendor class and get the desired enum value
        EDbVendor = jpype.JClass("gudusoft.gsqlparser.EDbVendor")
        database_vendor = EDbVendor.valueOf("dbvoracle")  # Replace with the desired database vendor

        # Create an instance of TGSqlParser with the specified database vendor
        sqlparser = TGSqlParser(database_vendor)

        # Set the SQL filename
        sqlparser.sqlfilename = file_path

        # Parse the SQL file
        ret = sqlparser.parse()
        if ret == 0:
            # Set formatting options
            option = GFmtOptFactory.newInstance()
            option.wsPaddingParenthesesInExpression = False

            # Format the SQL
            formatted_sql = FormatterFactory.pp(sqlparser, option)
            # return formatted_sql
            print(formatted_sql)
        else:
            print(f"Parsing failed. Error message: {sqlparser.getErrormessage()}")

    finally:
        # Shutdown the JVM when done
        jpype.shutdownJVM()

if __name__ == "__main__":
    sql_file_path = r"D:\wjp\testpy\testsqlfiles\demo.sql"
    
    format_sql(sql_file_path, "dbvoracle")  # Replace with the desired database vendor
