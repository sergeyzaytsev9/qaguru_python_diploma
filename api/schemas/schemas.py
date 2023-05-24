from voluptuous import Schema, ALLOW_EXTRA, Any

SUCCESSFUL = 200

token = Schema({
    "success": bool,
    "data": {
        "access": str,
        "refresh": str}
},
     extra=ALLOW_EXTRA)

create_base = Schema({
    "success": bool,
    "data": {
        "message": str,
    }
},
     extra=ALLOW_EXTRA)


get_bases_list = Schema({
    "success": bool,
    "data": {
        "bases": [{
            "owner": str,
            "originalPath": str,
            "originalName": str,
            "platform": str,
            "updateLog": Any(str, None),
            "needGb": Any(str, None),
            "download": str,
            "accessForDeveloper": Any(str, None),
            "name": str,
            "size": int,
            "path": str,
            "publicWeb": bool,
            "publicWebName": str,
            "publicWebPath": str,
            "publicWebState": bool,
            "publicWebAccess": bool,
            "autoUpdate": bool,
            "autoUpdateID": Any(str, None),
            "type": str,
            "dopList": [{
                "ID": Any(str, int),
                "LOGIN": str,
                "FIO": Any(str, None),
                "IS_MAIN_USER": str,
                "db_title": str
            }],
            "canReName": bool,
            "baseStatus": int,
            "cdnLock": str,
            "creationDatetime": str,
            "host": str,
            "autoUpdatePath": str
        }]}
}, extra=ALLOW_EXTRA)

get_gb_details = Schema(
    {
        "success": bool,
        "data": {
            "total": int,
            "available": int,
            "deactivation": int,
            "waitPay": int,
            "details": [
                {
                    "status": str,
                    "name": str,
                    "amount": int,
                    "endDate": Any(str, None),
                    "orderId": int,
                    "activated": bool,
                    "type": str,
                    "login": str,
                    None: Any(None, str)
                }
            ]
        },
    },
    extra=ALLOW_EXTRA,
)


