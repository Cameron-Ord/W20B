import mariadb
import dbcreds

def run_proceedure(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.ProgrammingError as error:
        print('There is an issue with the DB code: ', error)
    except mariadb.OperationalError:
        print('DB connection issue: ')
    except Exception as error:
        print("Unknown error: ", error)
    finally:
        if(cursor !=None):
            cursor.close()
        if(conn !=None):
            conn.close()
        return results
