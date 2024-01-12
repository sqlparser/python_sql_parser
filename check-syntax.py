# python_script.py
import jpype

def create_parser(vendor):
    TGSqlParser = jpype.JClass("gudusoft.gsqlparser.TGSqlParser")
    
    # Convert the vendor string to the corresponding EDbVendor value
    EDbVendor = jpype.JClass("gudusoft.gsqlparser.EDbVendor")
    db_vendor = getattr(EDbVendor, vendor)

    # Create an instance of TGSqlParser with EDbVendor as a parameter
    parser = TGSqlParser(db_vendor)

    return parser

def call_parse_method(sql, vendor):
    # Start the Java Virtual Machine (JVM)
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=C:\\prg\\gsp_demo_java\\lib\\gudusoft.gsqlparser-2.7.1.6.jar")

    try:
        # Create an instance of TGSqlParser based on the selected vendor
        parser = create_parser(vendor)

        # Set the SQL text
        parser.sqltext = sql

        # Call the parse() method
        result = parser.parse()

        if result == 0:
            print("Parsing successful")
        else:
            # Parsing failed, print the error message
            error_message = parser.getErrormessage()
            print(f"Parsing failed. Error message: {error_message}")

    finally:
        # Shutdown the JVM when done
        jpype.shutdownJVM()
        
     

if __name__ == "__main__":
    sql_query = "SELECT * FROM my_table;"
    database_vendor = "dbvoracle"  # Replace with the desired database vendor
    call_parse_method(sql_query, database_vendor)
