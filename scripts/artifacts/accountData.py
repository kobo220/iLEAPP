__artifacts_v2__ = {
    "accountData": {
        "name": "Account Data",
        "description": "Configured user accounts",
        "author": "@AlexisBrignoni",
        "version": "0.4.3",
        "date": "2020-04-30",
        "requirements": "none",
        "category": "Accounts",
        "notes": "",
        "paths": ('*/mobile/Library/Accounts/Accounts3.sqlite*',),
        "output_types": "standard"
    }
}


from scripts.ilapfuncs import artifact_processor, open_sqlite_db_readonly, convert_ts_human_to_timezone_offset

@artifact_processor
def accountData(files_found, report_folder, seeker, wrap_text, timezone_offset):
    data_list = []
    db_file = ''

    for file_found in files_found:
        if file_found.endswith('Accounts3.sqlite'):
            db_file = file_found
            break
    
    with open_sqlite_db_readonly(db_file) as db:
        cursor = db.cursor()
        cursor.execute('''
        SELECT
            datetime(zdate+978307200,'unixepoch'),
            zaccounttypedescription,
            zusername,
            zaccountdescription,
            zaccount.zidentifier,
            zaccount.zowningbundleid
        FROM zaccount, zaccounttype 
        WHERE zaccounttype.z_pk=zaccount.zaccounttype
        ''')

        all_rows = cursor.fetchall()

        for row in all_rows:
            timestamp = convert_ts_human_to_timezone_offset(row[0], timezone_offset)
            data_list.append((timestamp,row[1],row[2],row[3],row[4],row[5]))                

    data_headers = (
        ('Timestamp', 'datetime'), 
        'Account Desc.', 
        'Username', 
        'Description', 
        'Identifier', 
        'Bundle ID'
        )
    return data_headers, data_list, db_file
