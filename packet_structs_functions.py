def print_AC_ACCEPT_LOGIN(v):
  print('Fields of AC_ACCEPT_LOGIN:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - AID: {v.AID}")
  print(f" - userLevel: {v.userLevel}")
  print(f" - lastLoginIP: {v.lastLoginIP}")
  print(f" - lastLoginTime: {v.lastLoginTime}")
  print(f" - Sex: {v.Sex}")
  print(f" - server_list: {v.server_list}")

def print_AC_ACCEPT_LOGIN2(v):
  print('Fields of AC_ACCEPT_LOGIN2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - AID: {v.AID}")
  print(f" - userLevel: {v.userLevel}")
  print(f" - lastLoginIP: {v.lastLoginIP}")
  print(f" - lastLoginTime: {v.lastLoginTime}")
  print(f" - Sex: {v.Sex}")
  print(f" - iAccountSID: {v.iAccountSID}")

def print_AC_ACCEPT_LOGIN_SUB(v):
  print('Fields of AC_ACCEPT_LOGIN_SUB:')
  print(f" - packetId: {v.packetId}")
  print(f" - ip: {v.ip}")
  print(f" - port: {v.port}")
  print(f" - name: {v.name}")
  print(f" - usercount: {v.usercount}")
  print(f" - state: {v.state}")
  print(f" - property: {v.property}")

def print_AC_ACK_AUTHEKEY_FAIL_NOTMATCHCARDPASS(v):
  print('Fields of AC_ACK_AUTHEKEY_FAIL_NOTMATCHCARDPASS:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_AUTHREFUSE(v):
  print('Fields of AC_ACK_EKEY_FAIL_AUTHREFUSE:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_INPUTEKEY(v):
  print('Fields of AC_ACK_EKEY_FAIL_INPUTEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_NEEDCARDPASS(v):
  print('Fields of AC_ACK_EKEY_FAIL_NEEDCARDPASS:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_NOTEXIST(v):
  print('Fields of AC_ACK_EKEY_FAIL_NOTEXIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_NOTICE(v):
  print('Fields of AC_ACK_EKEY_FAIL_NOTICE:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_NOTUSEDEKEY(v):
  print('Fields of AC_ACK_EKEY_FAIL_NOTUSEDEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_EKEY_FAIL_NOTUSESEKEY(v):
  print('Fields of AC_ACK_EKEY_FAIL_NOTUSESEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_AC_ACK_FIRST_LOGIN(v):
  print('Fields of AC_ACK_FIRST_LOGIN:')
  print(f" - packetId: {v.packetId}")

def print_AC_ACK_GAME_GUARD(v):
  print('Fields of AC_ACK_GAME_GUARD:')
  print(f" - packetId: {v.packetId}")
  print(f" - ucAnswer: {v.ucAnswer}")

def print_AC_ACK_HASH(v):
  print('Fields of AC_ACK_HASH:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - secret: {v.secret}")

def print_AC_ACK_PT_ID_INFO(v):
  print('Fields of AC_ACK_PT_ID_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - szPTID: {v.szPTID}")
  print(f" - szPTNumID: {v.szPTNumID}")

def print_AC_ASK_PNGAMEROOM(v):
  print('Fields of AC_ASK_PNGAMEROOM:')
  print(f" - packetId: {v.packetId}")

def print_AC_EVENT_RESULT(v):
  print('Fields of AC_EVENT_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - EventItemCount: {v.EventItemCount}")

def print_AC_NOTIFY_ERROR(v):
  print('Fields of AC_NOTIFY_ERROR:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_AC_OTP_AUTH_ACK(v):
  print('Fields of AC_OTP_AUTH_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - LoginResult: {v.LoginResult}")

def print_AC_OTP_USER(v):
  print('Fields of AC_OTP_USER:')
  print(f" - packetId: {v.packetId}")

def print_AC_REFUSE_LOGIN(v):
  print('Fields of AC_REFUSE_LOGIN:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")
  print(f" - blockDate: {v.blockDate}")

def print_AC_REFUSE_LOGIN3(v):
  print('Fields of AC_REFUSE_LOGIN3:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")
  print(f" - BlockedReaminSEC: {v.BlockedReaminSEC}")

def print_AC_REFUSE_LOGIN_R2(v):
  print('Fields of AC_REFUSE_LOGIN_R2:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")
  print(f" - blockDate: {v.blockDate}")

def print_AC_REQUEST_SECOND_PASSWORD(v):
  print('Fields of AC_REQUEST_SECOND_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - dwSeed: {v.dwSeed}")

def print_AC_REQ_LOGIN_ACCOUNT_INFO(v):
  print('Fields of AC_REQ_LOGIN_ACCOUNT_INFO:')
  print(f" - packetId: {v.packetId}")

def print_AC_REQ_LOGIN_CARDPASS(v):
  print('Fields of AC_REQ_LOGIN_CARDPASS:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_SeedValue: {v.m_SeedValue}")

def print_AC_REQ_LOGIN_NEWEKEY(v):
  print('Fields of AC_REQ_LOGIN_NEWEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_SeedValue: {v.m_SeedValue}")

def print_AC_REQ_LOGIN_OLDEKEY(v):
  print('Fields of AC_REQ_LOGIN_OLDEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_SeedValue: {v.m_SeedValue}")

def print_AC_REQ_MOBILE_OTP(v):
  print('Fields of AC_REQ_MOBILE_OTP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_AC_REQ_NEW_USER(v):
  print('Fields of AC_REQ_NEW_USER:')
  print(f" - packetId: {v.packetId}")

def print_AC_SHUTDOWN_INFO(v):
  print('Fields of AC_SHUTDOWN_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - Time: {v.Time}")

def print_AC_SHUTDOWN_NOTIFY(v):
  print('Fields of AC_SHUTDOWN_NOTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - Time: {v.Time}")
  print(f" - ServerTime: {v.ServerTime}")

def print_AC_SSO_LOGIN_ACK(v):
  print('Fields of AC_SSO_LOGIN_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_CAH_ACK_GAME_GUARD(v):
  print('Fields of CAH_ACK_GAME_GUARD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AuthData: {v.AuthData}")

def print_CA_ACK_LOGIN_ACCOUNT_INFO(v):
  print('Fields of CA_ACK_LOGIN_ACCOUNT_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - sex: {v.sex}")
  print(f" - bPoint: {v.bPoint}")
  print(f" - E_mail: {v.E_mail}")

def print_CA_ACK_LOGIN_CARDPASS(v):
  print('Fields of CA_ACK_LOGIN_CARDPASS:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_cardPass: {v.m_cardPass}")

def print_CA_ACK_LOGIN_NEWEKEY(v):
  print('Fields of CA_ACK_LOGIN_NEWEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_SeedValue: {v.m_SeedValue}")
  print(f" - m_EKey: {v.m_EKey}")

def print_CA_ACK_LOGIN_OLDEKEY(v):
  print('Fields of CA_ACK_LOGIN_OLDEKEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_SeedValue: {v.m_SeedValue}")
  print(f" - m_EKey: {v.m_EKey}")

def print_CA_ACK_NEW_USER(v):
  print('Fields of CA_ACK_NEW_USER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Sex: {v.Sex}")

def print_CA_CLIENT_TYPE(v):
  print('Fields of CA_CLIENT_TYPE:')
  print(f" - packetId: {v.packetId}")
  print(f" - ClientType: {v.ClientType}")
  print(f" - nVer: {v.nVer}")

def print_CA_CONNECT_INFO_CHANGED(v):
  print('Fields of CA_CONNECT_INFO_CHANGED:')
  print(f" - packetId: {v.packetId}")
  print(f" - ID: {v.ID}")

def print_CA_EXE_HASHCHECK(v):
  print('Fields of CA_EXE_HASHCHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - HashValue: {v.HashValue}")

def print_CA_LOGIN(v):
  print('Fields of CA_LOGIN:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - Passwd: {v.Passwd}")
  print(f" - clienttype: {v.clienttype}")

def print_CA_LOGIN2(v):
  print('Fields of CA_LOGIN2:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - PasswdMD5: {v.PasswdMD5}")
  print(f" - clienttype: {v.clienttype}")

def print_CA_LOGIN3(v):
  print('Fields of CA_LOGIN3:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - PasswdMD5: {v.PasswdMD5}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - ClientInfo: {v.ClientInfo}")

def print_CA_LOGIN4(v):
  print('Fields of CA_LOGIN4:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - PasswdMD5: {v.PasswdMD5}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - macData: {v.macData}")

def print_CA_LOGIN5(v):
  print('Fields of CA_LOGIN5:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - Passwd: {v.Passwd}")
  print(f" - clienttype: {v.clienttype}")

def print_CA_LOGIN6(v):
  print('Fields of CA_LOGIN6:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - PasswdMD5: {v.PasswdMD5}")
  print(f" - clienttype: {v.clienttype}")

def print_CA_LOGIN_HAN(v):
  print('Fields of CA_LOGIN_HAN:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - Passwd: {v.Passwd}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - m_szIP: {v.m_szIP}")
  print(f" - m_szMacAddr: {v.m_szMacAddr}")
  print(f" - isHanGameUser: {v.isHanGameUser}")

def print_CA_LOGIN_OTP(v):
  print('Fields of CA_LOGIN_OTP:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Version: {v.Version}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - TransactionID: {v.TransactionID}")

def print_CA_LOGIN_PCBANG(v):
  print('Fields of CA_LOGIN_PCBANG:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - ID: {v.ID}")
  print(f" - Passwd: {v.Passwd}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - IP: {v.IP}")
  print(f" - MacAdress: {v.MacAdress}")

def print_CA_OTP_AUTH_REQ(v):
  print('Fields of CA_OTP_AUTH_REQ:')
  print(f" - packetId: {v.packetId}")
  print(f" - OTPCode: {v.OTPCode}")

def print_CA_REPLY_PNGAMEROOM(v):
  print('Fields of CA_REPLY_PNGAMEROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Permission: {v.Permission}")

def print_CA_REQ_GAME_GUARD_CHECK(v):
  print('Fields of CA_REQ_GAME_GUARD_CHECK:')
  print(f" - packetId: {v.packetId}")

def print_CA_REQ_HASH(v):
  print('Fields of CA_REQ_HASH:')
  print(f" - packetId: {v.packetId}")

def print_CA_SSO_LOGIN_REQ(v):
  print('Fields of CA_SSO_LOGIN_REQ:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Version: {v.Version}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - ID: {v.ID}")
  print(f" - Passwd: {v.Passwd}")
  print(f" - MacAdress: {v.MacAdress}")
  print(f" - IP: {v.IP}")
  print(f" - t1: {v.t1}")

def print_CA_SSO_LOGIN_REQa(v):
  print('Fields of CA_SSO_LOGIN_REQa:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Version: {v.Version}")
  print(f" - clienttype: {v.clienttype}")
  print(f" - ID: {v.ID}")
  print(f" - MacAddr: {v.MacAddr}")
  print(f" - IpAddr: {v.IpAddr}")
  print(f" - t1: {v.t1}")

def print_CH_AVAILABLE_SECOND_PASSWD(v):
  print('Fields of CH_AVAILABLE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CH_CHARLIST_REQ(v):
  print('Fields of CH_CHARLIST_REQ:')
  print(f" - packetId: {v.packetId}")

def print_CH_CHECKBOT(v):
  print('Fields of CH_CHECKBOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - dwAID: {v.dwAID}")
  print(f" - szStringInfo: {v.szStringInfo}")

def print_CH_DELETE_CHAR(v):
  print('Fields of CH_DELETE_CHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - key: {v.key}")

def print_CH_DELETE_CHAR2(v):
  print('Fields of CH_DELETE_CHAR2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - key: {v.key}")

def print_CH_DELETE_CHAR3(v):
  print('Fields of CH_DELETE_CHAR3:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - Birth: {v.Birth}")

def print_CH_DELETE_CHAR3_CANCEL(v):
  print('Fields of CH_DELETE_CHAR3_CANCEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CH_DELETE_CHAR3_RESERVED(v):
  print('Fields of CH_DELETE_CHAR3_RESERVED:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CH_DELETE_SECOND_PASSWD(v):
  print('Fields of CH_DELETE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Seed: {v.Seed}")
  print(f" - SecondPWIdx: {v.SecondPWIdx}")

def print_CH_EDIT_SECOND_PASSWD(v):
  print('Fields of CH_EDIT_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Seed: {v.Seed}")
  print(f" - SecondPWIdx: {v.SecondPWIdx}")

def print_CH_ENTER(v):
  print('Fields of CH_ENTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - userLevel: {v.userLevel}")
  print(f" - clientType: {v.clientType}")
  print(f" - Sex: {v.Sex}")

def print_CH_ENTER2(v):
  print('Fields of CH_ENTER2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - userLevel: {v.userLevel}")
  print(f" - clientType: {v.clientType}")
  print(f" - Sex: {v.Sex}")
  print(f" - macData: {v.macData}")
  print(f" - iAccountSID: {v.iAccountSID}")

def print_CH_ENTER_CHECKBOT(v):
  print('Fields of CH_ENTER_CHECKBOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - dwAID: {v.dwAID}")
  print(f" - szStringInfo: {v.szStringInfo}")

def print_CH_EXE_HASHCHECK(v):
  print('Fields of CH_EXE_HASHCHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - ClientType: {v.ClientType}")
  print(f" - HashValue: {v.HashValue}")

def print_CH_MAKE_CHAR(v):
  print('Fields of CH_MAKE_CHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")
  print(f" - Str: {v.Str}")
  print(f" - Agi: {v.Agi}")
  print(f" - Vit: {v.Vit}")
  print(f" - Int: {v.Int}")
  print(f" - Dex: {v.Dex}")
  print(f" - Luk: {v.Luk}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - headPal: {v.headPal}")
  print(f" - head: {v.head}")

def print_CH_MAKE_CHAR_NOT_STATS(v):
  print('Fields of CH_MAKE_CHAR_NOT_STATS:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - headPal: {v.headPal}")
  print(f" - head: {v.head}")

def print_CH_MAKE_SECOND_PASSWD(v):
  print('Fields of CH_MAKE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Seed: {v.Seed}")
  print(f" - SecondPWIdx: {v.SecondPWIdx}")

def print_CH_NOT_AVAILABLE_SECOND_PASSWD(v):
  print('Fields of CH_NOT_AVAILABLE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - SecondPWIdx: {v.SecondPWIdx}")

def print_CH_REQ_CHANGE_CHARACTERNAME(v):
  print('Fields of CH_REQ_CHANGE_CHARACTERNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - dwGID: {v.dwGID}")
  print(f" - szCharName: {v.szCharName}")

def print_CH_REQ_CHANGE_CHARACTER_SLOT(v):
  print('Fields of CH_REQ_CHANGE_CHARACTER_SLOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - beforeCharNum: {v.beforeCharNum}")
  print(f" - AfterCharNum: {v.AfterCharNum}")
  print(f" - CurChrSlotCnt: {v.CurChrSlotCnt}")

def print_CH_REQ_CHANGE_CHARNAME(v):
  print('Fields of CH_REQ_CHANGE_CHARNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - dwGID: {v.dwGID}")

def print_CH_REQ_CHARINFO_PER_PAGE(v):
  print('Fields of CH_REQ_CHARINFO_PER_PAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - SeqNum: {v.SeqNum}")

def print_CH_REQ_IS_VALID_CHARNAME(v):
  print('Fields of CH_REQ_IS_VALID_CHARNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - dwAID: {v.dwAID}")
  print(f" - dwGID: {v.dwGID}")
  print(f" - szCharName: {v.szCharName}")

def print_CH_SECOND_PASSWD_ACK(v):
  print('Fields of CH_SECOND_PASSWD_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - SecondPWIdx: {v.SecondPWIdx}")

def print_CH_SELECT_ACCESSIBLE_MAPNAME(v):
  print('Fields of CH_SELECT_ACCESSIBLE_MAPNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - mapListNum: {v.mapListNum}")

def print_CH_SELECT_CHAR(v):
  print('Fields of CH_SELECT_CHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - CharNum: {v.CharNum}")

def print_CH_SELECT_CHAR_GOINGTOBEUSED(v):
  print('Fields of CH_SELECT_CHAR_GOINGTOBEUSED:')
  print(f" - packetId: {v.packetId}")
  print(f" - dwAID: {v.dwAID}")
  print(f" - nCountSelectedChar: {v.nCountSelectedChar}")
  print(f" - ardwSelectedGID: {v.ardwSelectedGID}")

def print_CH_WAITING_LOGIN(v):
  print('Fields of CH_WAITING_LOGIN:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - userLevel: {v.userLevel}")
  print(f" - clientType: {v.clientType}")
  print(f" - Sex: {v.Sex}")

def print_COLLECTORDEAD(v):
  print('Fields of COLLECTORDEAD:')
  print(f" - packetId: {v.packetId}")
  print(f" - ServerID: {v.ServerID}")

def print_CS_LOGIN_QUERY(v):
  print('Fields of CS_LOGIN_QUERY:')
  print(f" - packetId: {v.packetId}")
  print(f" - Version: {v.Version}")
  print(f" - i64SteamID: {v.i64SteamID}")
  print(f" - ticketLength: {v.ticketLength}")
  print(f" - AuthTicket: {v.AuthTicket}")

def print_CS_REQ_ENCRYPTION(v):
  print('Fields of CS_REQ_ENCRYPTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - encCount: {v.encCount}")
  print(f" - decCount: {v.decCount}")

def print_CZ_ACK_AU_BOT(v):
  print('Fields of CZ_ACK_AU_BOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CZ_ACK_CASH_PASSWORD(v):
  print('Fields of CZ_ACK_CASH_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")
  print(f" - Password: {v.Password}")
  print(f" - NewPassword: {v.NewPassword}")

def print_CZ_ACK_EXCHANGE_ITEM(v):
  print('Fields of CZ_ACK_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_CZ_ACK_GAME_GUARD(v):
  print('Fields of CZ_ACK_GAME_GUARD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AuthData: {v.AuthData}")

def print_CZ_ACK_REQ_ADD_FRIENDS(v):
  print('Fields of CZ_ACK_REQ_ADD_FRIENDS:')
  print(f" - packetId: {v.packetId}")
  print(f" - ReqAID: {v.ReqAID}")
  print(f" - ReqGID: {v.ReqGID}")
  print(f" - Result: {v.Result}")

def print_CZ_ACK_SELECT_DEALTYPE(v):
  print('Fields of CZ_ACK_SELECT_DEALTYPE:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")
  print(f" - type: {v.type}")

def print_CZ_ACK_STORE_PASSWORD(v):
  print('Fields of CZ_ACK_STORE_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")
  print(f" - Password: {v.Password}")
  print(f" - NewPassword: {v.NewPassword}")

def print_CZ_ACTIVE_QUEST(v):
  print('Fields of CZ_ACTIVE_QUEST:')
  print(f" - packetId: {v.packetId}")
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")

def print_CZ_ADD_EXCHANGE_ITEM(v):
  print('Fields of CZ_ADD_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_ADD_FRIENDS(v):
  print('Fields of CZ_ADD_FRIENDS:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")

def print_CZ_AGREE_STARPLACE(v):
  print('Fields of CZ_AGREE_STARPLACE:')
  print(f" - packetId: {v.packetId}")
  print(f" - which: {v.which}")

def print_CZ_ALCHEMIST_RANK(v):
  print('Fields of CZ_ALCHEMIST_RANK:')
  print(f" - packetId: {v.packetId}")

def print_CZ_ALLY_GUILD(v):
  print('Fields of CZ_ALLY_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - otherAID: {v.otherAID}")
  print(f" - answer: {v.answer}")

def print_CZ_AUCTION_ADD(v):
  print('Fields of CZ_AUCTION_ADD:')
  print(f" - packetId: {v.packetId}")
  print(f" - NowMoney: {v.NowMoney}")
  print(f" - MaxMoney: {v.MaxMoney}")
  print(f" - DeleteHour: {v.DeleteHour}")

def print_CZ_AUCTION_ADD_CANCEL(v):
  print('Fields of CZ_AUCTION_ADD_CANCEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - AuctionID: {v.AuctionID}")

def print_CZ_AUCTION_ADD_ITEM(v):
  print('Fields of CZ_AUCTION_ADD_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_AUCTION_BUY(v):
  print('Fields of CZ_AUCTION_BUY:')
  print(f" - packetId: {v.packetId}")
  print(f" - AuctionID: {v.AuctionID}")
  print(f" - Money: {v.Money}")

def print_CZ_AUCTION_CREATE(v):
  print('Fields of CZ_AUCTION_CREATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_CZ_AUCTION_ITEM_SEARCH(v):
  print('Fields of CZ_AUCTION_ITEM_SEARCH:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")
  print(f" - AuctionID: {v.AuctionID}")
  print(f" - Name: {v.Name}")
  print(f" - Page: {v.Page}")

def print_CZ_AUCTION_REQ_MY_INFO(v):
  print('Fields of CZ_AUCTION_REQ_MY_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_CZ_AUCTION_REQ_MY_SELL_STOP(v):
  print('Fields of CZ_AUCTION_REQ_MY_SELL_STOP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AuctionID: {v.AuctionID}")

def print_CZ_BATTLEFIELD_CHAT(v):
  print('Fields of CZ_BATTLEFIELD_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_CZ_BATTLE_FIELD_LIST(v):
  print('Fields of CZ_BATTLE_FIELD_LIST:')
  print(f" - packetId: {v.packetId}")

def print_CZ_BLACKSMITH_RANK(v):
  print('Fields of CZ_BLACKSMITH_RANK:')
  print(f" - packetId: {v.packetId}")

def print_CZ_BLOCKING_PLAY_CANCEL(v):
  print('Fields of CZ_BLOCKING_PLAY_CANCEL:')
  print(f" - packetId: {v.packetId}")

def print_CZ_BOT_CHECK(v):
  print('Fields of CZ_BOT_CHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - IsBot: {v.IsBot}")

def print_CZ_BROADCAST(v):
  print('Fields of CZ_BROADCAST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_CZ_CANCEL_BATTLE_FIELD(v):
  print('Fields of CZ_CANCEL_BATTLE_FIELD:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")

def print_CZ_CANCEL_EXCHANGE_ITEM(v):
  print('Fields of CZ_CANCEL_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CANCEL_LOCKON(v):
  print('Fields of CZ_CANCEL_LOCKON:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CANCEL_MERGE_ITEM(v):
  print('Fields of CZ_CANCEL_MERGE_ITEM:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CHANGE_CHATROOM(v):
  print('Fields of CZ_CHANGE_CHATROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - size: {v.size}")
  print(f" - type: {v.type}")
  print(f" - passwd: {v.passwd}")
  print(f" - title: {v.title}")

def print_CZ_CHANGE_DIRECTION(v):
  print('Fields of CZ_CHANGE_DIRECTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - headDir: {v.headDir}")
  print(f" - dir: {v.dir}")

def print_CZ_CHANGE_DIRECTION2(v):
  print('Fields of CZ_CHANGE_DIRECTION2:')
  print(f" - packetId: {v.packetId}")
  print(f" - headDir: {v.headDir}")
  print(f" - dir: {v.dir}")

def print_CZ_CHANGE_EFFECTSTATE(v):
  print('Fields of CZ_CHANGE_EFFECTSTATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - EffectState: {v.EffectState}")

def print_CZ_CHANGE_GROUPEXPOPTION(v):
  print('Fields of CZ_CHANGE_GROUPEXPOPTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - expOption: {v.expOption}")

def print_CZ_CHANGE_GROUP_MASTER(v):
  print('Fields of CZ_CHANGE_GROUP_MASTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_CHANGE_MAPTYPE(v):
  print('Fields of CZ_CHANGE_MAPTYPE:')
  print(f" - packetId: {v.packetId}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - type: {v.type}")

def print_CZ_CHECK_RECEIVE_CHARACTER_NAME(v):
  print('Fields of CZ_CHECK_RECEIVE_CHARACTER_NAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - receiveName: {v.receiveName}")

def print_CZ_CHOOSE_MENU(v):
  print('Fields of CZ_CHOOSE_MENU:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")
  print(f" - num: {v.num}")

def print_CZ_CHOPOKGI(v):
  print('Fields of CZ_CHOPOKGI:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CLAN_CHAT(v):
  print('Fields of CZ_CLAN_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - chat: {v.chat}")

def print_CZ_CLIENT_VERSION(v):
  print('Fields of CZ_CLIENT_VERSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - clientVer: {v.clientVer}")

def print_CZ_CLOSE_BARGAIN_SALE_TOOL(v):
  print('Fields of CZ_CLOSE_BARGAIN_SALE_TOOL:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_CLOSE_DIALOG(v):
  print('Fields of CZ_CLOSE_DIALOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_CZ_CLOSE_MAILBOX(v):
  print('Fields of CZ_CLOSE_MAILBOX:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CLOSE_SEARCH_STORE_INFO(v):
  print('Fields of CZ_CLOSE_SEARCH_STORE_INFO:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CLOSE_SIMPLECASH_SHOP(v):
  print('Fields of CZ_CLOSE_SIMPLECASH_SHOP:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CLOSE_STORE(v):
  print('Fields of CZ_CLOSE_STORE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CLOSE_WINDOW(v):
  print('Fields of CZ_CLOSE_WINDOW:')
  print(f" - packetId: {v.packetId}")

def print_CZ_COMMAND_MER(v):
  print('Fields of CZ_COMMAND_MER:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - command: {v.command}")

def print_CZ_COMMAND_PET(v):
  print('Fields of CZ_COMMAND_PET:')
  print(f" - packetId: {v.packetId}")
  print(f" - cSub: {v.cSub}")

def print_CZ_CONCLUDE_EXCHANGE_ITEM(v):
  print('Fields of CZ_CONCLUDE_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")

def print_CZ_CONFIG(v):
  print('Fields of CZ_CONFIG:')
  print(f" - packetId: {v.packetId}")
  print(f" - Config: {v.Config}")
  print(f" - Value: {v.Value}")

def print_CZ_CONTACTNPC(v):
  print('Fields of CZ_CONTACTNPC:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")
  print(f" - type: {v.type}")

def print_CZ_CREATE_CHATROOM(v):
  print('Fields of CZ_CREATE_CHATROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - size: {v.size}")
  print(f" - type: {v.type}")
  print(f" - passwd: {v.passwd}")
  print(f" - title: {v.title}")

def print_CZ_DEATH_QUESTION(v):
  print('Fields of CZ_DEATH_QUESTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - Qanswer: {v.Qanswer}")

def print_CZ_DELETE_FRIENDS(v):
  print('Fields of CZ_DELETE_FRIENDS:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")

def print_CZ_DISCONNECT_ALL_CHARACTER(v):
  print('Fields of CZ_DISCONNECT_ALL_CHARACTER:')
  print(f" - packetId: {v.packetId}")

def print_CZ_DISCONNECT_CHARACTER(v):
  print('Fields of CZ_DISCONNECT_CHARACTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_DORIDORI(v):
  print('Fields of CZ_DORIDORI:')
  print(f" - packetId: {v.packetId}")

def print_CZ_DYNAMICNPC_CREATE_REQUEST(v):
  print('Fields of CZ_DYNAMICNPC_CREATE_REQUEST:')
  print(f" - packetId: {v.packetId}")
  print(f" - NickName: {v.NickName}")

def print_CZ_ENTER(v):
  print('Fields of CZ_ENTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - clientTime: {v.clientTime}")
  print(f" - Sex: {v.Sex}")

def print_CZ_ENTER2(v):
  print('Fields of CZ_ENTER2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - AuthCode: {v.AuthCode}")
  print(f" - clientTime: {v.clientTime}")
  print(f" - Sex: {v.Sex}")

def print_CZ_EQUIPWIN_MICROSCOPE(v):
  print('Fields of CZ_EQUIPWIN_MICROSCOPE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_ES_CANCEL(v):
  print('Fields of CZ_ES_CANCEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - esNo: {v.esNo}")

def print_CZ_ES_CHOOSE(v):
  print('Fields of CZ_ES_CHOOSE:')
  print(f" - packetId: {v.packetId}")
  print(f" - esNo: {v.esNo}")

def print_CZ_ES_GET_LIST(v):
  print('Fields of CZ_ES_GET_LIST:')
  print(f" - packetId: {v.packetId}")

def print_CZ_EXEC_EXCHANGE_ITEM(v):
  print('Fields of CZ_EXEC_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")

def print_CZ_EXE_HASHCHECK(v):
  print('Fields of CZ_EXE_HASHCHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - ClientType: {v.ClientType}")
  print(f" - HashValue: {v.HashValue}")

def print_CZ_EXIT_ROOM(v):
  print('Fields of CZ_EXIT_ROOM:')
  print(f" - packetId: {v.packetId}")

def print_CZ_GANGSI_RANK(v):
  print('Fields of CZ_GANGSI_RANK:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketSwitch: {v.PacketSwitch}")

def print_CZ_GM_FULLSTRIP(v):
  print('Fields of CZ_GM_FULLSTRIP:')
  print(f" - packetId: {v.packetId}")
  print(f" - TargetAID: {v.TargetAID}")

def print_CZ_GPK_DYNCODE_RELOAD(v):
  print('Fields of CZ_GPK_DYNCODE_RELOAD:')
  print(f" - packetId: {v.packetId}")

def print_CZ_GROUPINFO_CHANGE_V2(v):
  print('Fields of CZ_GROUPINFO_CHANGE_V2:')
  print(f" - packetId: {v.packetId}")
  print(f" - expOption: {v.expOption}")
  print(f" - ItemPickupRule: {v.ItemPickupRule}")
  print(f" - ItemDivisionRule: {v.ItemDivisionRule}")

def print_CZ_GUILD_CHAT(v):
  print('Fields of CZ_GUILD_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_CZ_GUILD_NOTICE(v):
  print('Fields of CZ_GUILD_NOTICE:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - subject: {v.subject}")
  print(f" - notice: {v.notice}")

def print_CZ_GUILD_ZENY(v):
  print('Fields of CZ_GUILD_ZENY:')
  print(f" - packetId: {v.packetId}")
  print(f" - zeny: {v.zeny}")

def print_CZ_HUNTINGLIST(v):
  print('Fields of CZ_HUNTINGLIST:')
  print(f" - packetId: {v.packetId}")

def print_CZ_INPUT_EDITDLG(v):
  print('Fields of CZ_INPUT_EDITDLG:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")
  print(f" - value: {v.value}")

def print_CZ_INPUT_EDITDLGSTR(v):
  print('Fields of CZ_INPUT_EDITDLGSTR:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - NAID: {v.NAID}")
  print(f" - msg: {v.msg}")

def print_CZ_INVENTORY_TAB(v):
  print('Fields of CZ_INVENTORY_TAB:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - NORMALorPRIVATE: {v.NORMALorPRIVATE}")

def print_CZ_IRMAIL_LIST(v):
  print('Fields of CZ_IRMAIL_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - office: {v.office}")
  print(f" - id: {v.id}")

def print_CZ_IRMAIL_SEND(v):
  print('Fields of CZ_IRMAIL_SEND:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ReceiveName: {v.ReceiveName}")
  print(f" - Title: {v.Title}")
  print(f" - Zeny: {v.Zeny}")
  print(f" - index: {v.index}")
  print(f" - id: {v.id}")
  print(f" - cnt: {v.cnt}")

def print_CZ_ITEMLISTWIN_RES(v):
  print('Fields of CZ_ITEMLISTWIN_RES:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Type: {v.Type}")
  print(f" - Action: {v.Action}")
  print(f" - MaterialList: {v.MaterialList}")

def print_CZ_ITEM_CREATE(v):
  print('Fields of CZ_ITEM_CREATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - itemName: {v.itemName}")

def print_CZ_ITEM_CREATE_EX(v):
  print('Fields of CZ_ITEM_CREATE_EX:')
  print(f" - packetId: {v.packetId}")
  print(f" - itemName: {v.itemName}")

def print_CZ_ITEM_PICKUP(v):
  print('Fields of CZ_ITEM_PICKUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")

def print_CZ_ITEM_PICKUP2(v):
  print('Fields of CZ_ITEM_PICKUP2:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")

def print_CZ_ITEM_THROW(v):
  print('Fields of CZ_ITEM_THROW:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")

def print_CZ_ITEM_THROW2(v):
  print('Fields of CZ_ITEM_THROW2:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")

def print_CZ_JOIN_BABY(v):
  print('Fields of CZ_JOIN_BABY:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - answer: {v.answer}")

def print_CZ_JOIN_BATTLE_FIELD(v):
  print('Fields of CZ_JOIN_BATTLE_FIELD:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")
  print(f" - JoinTeam: {v.JoinTeam}")

def print_CZ_JOIN_COUPLE(v):
  print('Fields of CZ_JOIN_COUPLE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - answer: {v.answer}")

def print_CZ_JOIN_GROUP(v):
  print('Fields of CZ_JOIN_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - GRID: {v.GRID}")
  print(f" - answer: {v.answer}")

def print_CZ_JOIN_GUILD(v):
  print('Fields of CZ_JOIN_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - answer: {v.answer}")

def print_CZ_KSY_EVENT(v):
  print('Fields of CZ_KSY_EVENT:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_LESSEFFECT(v):
  print('Fields of CZ_LESSEFFECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - isLess: {v.isLess}")

def print_CZ_MACRO_ITEM_PICKUP(v):
  print('Fields of CZ_MACRO_ITEM_PICKUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")

def print_CZ_MACRO_REQUEST_ACT(v):
  print('Fields of CZ_MACRO_REQUEST_ACT:')
  print(f" - packetId: {v.packetId}")
  print(f" - action: {v.action}")
  print(f" - targetGID: {v.targetGID}")

def print_CZ_MACRO_REQUEST_MOVE(v):
  print('Fields of CZ_MACRO_REQUEST_MOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - dest: {v.dest}")

def print_CZ_MACRO_START(v):
  print('Fields of CZ_MACRO_START:')
  print(f" - packetId: {v.packetId}")

def print_CZ_MACRO_STOP(v):
  print('Fields of CZ_MACRO_STOP:')
  print(f" - packetId: {v.packetId}")

def print_CZ_MACRO_USE_SKILL(v):
  print('Fields of CZ_MACRO_USE_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - targetID: {v.targetID}")

def print_CZ_MACRO_USE_SKILL_TOGROUND(v):
  print('Fields of CZ_MACRO_USE_SKILL_TOGROUND:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_CZ_MAIL_ADD_ITEM(v):
  print('Fields of CZ_MAIL_ADD_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MAIL_DELETE(v):
  print('Fields of CZ_MAIL_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")

def print_CZ_MAIL_GET_ITEM(v):
  print('Fields of CZ_MAIL_GET_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")

def print_CZ_MAIL_GET_LIST(v):
  print('Fields of CZ_MAIL_GET_LIST:')
  print(f" - packetId: {v.packetId}")

def print_CZ_MAIL_OPEN(v):
  print('Fields of CZ_MAIL_OPEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")

def print_CZ_MAIL_RESET_ITEM(v):
  print('Fields of CZ_MAIL_RESET_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_CZ_MAIL_SEND(v):
  print('Fields of CZ_MAIL_SEND:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ReceiveName: {v.ReceiveName}")
  print(f" - Header: {v.Header}")
  print(f" - msg_len: {v.msg_len}")
  print(f" - msg: {v.msg}")

def print_CZ_MAKE_GROUP(v):
  print('Fields of CZ_MAKE_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - groupName: {v.groupName}")

def print_CZ_MAKE_GROUP2(v):
  print('Fields of CZ_MAKE_GROUP2:')
  print(f" - packetId: {v.packetId}")
  print(f" - groupName: {v.groupName}")
  print(f" - ItemPickupRule: {v.ItemPickupRule}")
  print(f" - ItemDivisionRule: {v.ItemDivisionRule}")

def print_CZ_MEMORIALDUNGEON_COMMAND(v):
  print('Fields of CZ_MEMORIALDUNGEON_COMMAND:')
  print(f" - packetId: {v.packetId}")
  print(f" - Command: {v.Command}")

def print_CZ_MER_COMMAND(v):
  print('Fields of CZ_MER_COMMAND:')
  print(f" - packetId: {v.packetId}")
  print(f" - command: {v.command}")

def print_CZ_MER_UPGRADE_SKILLLEVEL(v):
  print('Fields of CZ_MER_UPGRADE_SKILLLEVEL:')
  print(f" - SKID: {v.SKID}")

def print_CZ_MER_USE_SKILL(v):
  print('Fields of CZ_MER_USE_SKILL:')
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - targetID: {v.targetID}")

def print_CZ_MONSTER_TALK(v):
  print('Fields of CZ_MONSTER_TALK:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - stateId: {v.stateId}")
  print(f" - skillId: {v.skillId}")
  print(f" - arg1: {v.arg1}")

def print_CZ_MOVETO_MAP(v):
  print('Fields of CZ_MOVETO_MAP:')
  print(f" - packetId: {v.packetId}")
  print(f" - mapName: {v.mapName}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_CZ_MOVE_ITEM_FROM_BODY_TO_CART(v):
  print('Fields of CZ_MOVE_ITEM_FROM_BODY_TO_CART:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_BODY_TO_GUILDSTORAGE(v):
  print('Fields of CZ_MOVE_ITEM_FROM_BODY_TO_GUILDSTORAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_BODY_TO_STORE(v):
  print('Fields of CZ_MOVE_ITEM_FROM_BODY_TO_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_BODY_TO_STORE2(v):
  print('Fields of CZ_MOVE_ITEM_FROM_BODY_TO_STORE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_CART_TO_BODY(v):
  print('Fields of CZ_MOVE_ITEM_FROM_CART_TO_BODY:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_CART_TO_GUILDSTORAGE(v):
  print('Fields of CZ_MOVE_ITEM_FROM_CART_TO_GUILDSTORAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_CART_TO_STORE(v):
  print('Fields of CZ_MOVE_ITEM_FROM_CART_TO_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_GUILDSTORAGE_TO_BODY(v):
  print('Fields of CZ_MOVE_ITEM_FROM_GUILDSTORAGE_TO_BODY:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_GUILDSTORAGE_TO_CART(v):
  print('Fields of CZ_MOVE_ITEM_FROM_GUILDSTORAGE_TO_CART:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_STORE_TO_BODY(v):
  print('Fields of CZ_MOVE_ITEM_FROM_STORE_TO_BODY:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_STORE_TO_BODY2(v):
  print('Fields of CZ_MOVE_ITEM_FROM_STORE_TO_BODY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_MOVE_ITEM_FROM_STORE_TO_CART(v):
  print('Fields of CZ_MOVE_ITEM_FROM_STORE_TO_CART:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_NOTIFY_ACTORINIT(v):
  print('Fields of CZ_NOTIFY_ACTORINIT:')
  print(f" - packetId: {v.packetId}")

def print_CZ_NPC_MARKET_CLOSE(v):
  print('Fields of CZ_NPC_MARKET_CLOSE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_NPC_MARKET_PURCHASE(v):
  print('Fields of CZ_NPC_MARKET_PURCHASE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_CZ_NPC_TRADE_QUIT(v):
  print('Fields of CZ_NPC_TRADE_QUIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketTpye: {v.PacketTpye}")

def print_CZ_NPROTECTGAMEGUARDCSAUTH(v):
  print('Fields of CZ_NPROTECTGAMEGUARDCSAUTH:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_CZ_OPEN_BARGAIN_SALE_TOOL(v):
  print('Fields of CZ_OPEN_BARGAIN_SALE_TOOL:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_OPEN_MAILBOX(v):
  print('Fields of CZ_OPEN_MAILBOX:')
  print(f" - packetId: {v.packetId}")
  print(f" - opentype: {v.opentype}")
  print(f" - Upper_MailID: {v.Upper_MailID}")

def print_CZ_OPEN_SIMPLE_CASHSHOP_ITEMLIST(v):
  print('Fields of CZ_OPEN_SIMPLE_CASHSHOP_ITEMLIST:')
  print(f" - packetId: {v.packetId}")

def print_CZ_PARTY_BOOKING_REQ_DELETE(v):
  print('Fields of CZ_PARTY_BOOKING_REQ_DELETE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_PARTY_BOOKING_REQ_REGISTER(v):
  print('Fields of CZ_PARTY_BOOKING_REQ_REGISTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Level: {v.Level}")
  print(f" - MapID: {v.MapID}")
  print(f" - Job: {v.Job}")

def print_CZ_PARTY_BOOKING_REQ_SEARCH(v):
  print('Fields of CZ_PARTY_BOOKING_REQ_SEARCH:')
  print(f" - packetId: {v.packetId}")
  print(f" - Level: {v.Level}")
  print(f" - MapID: {v.MapID}")
  print(f" - Job: {v.Job}")
  print(f" - LastIndex: {v.LastIndex}")
  print(f" - ResultCount: {v.ResultCount}")

def print_CZ_PARTY_BOOKING_REQ_UPDATE(v):
  print('Fields of CZ_PARTY_BOOKING_REQ_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Job: {v.Job}")

def print_CZ_PARTY_CONFIG(v):
  print('Fields of CZ_PARTY_CONFIG:')
  print(f" - packetId: {v.packetId}")
  print(f" - bRefuseJoinMsg: {v.bRefuseJoinMsg}")

def print_CZ_PARTY_JOIN_REQ(v):
  print('Fields of CZ_PARTY_JOIN_REQ:')
  print(f" - packetId: {v.packetId}")
  print(f" - characterName: {v.characterName}")

def print_CZ_PARTY_JOIN_REQ_ACK(v):
  print('Fields of CZ_PARTY_JOIN_REQ_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - GRID: {v.GRID}")
  print(f" - bAccept: {v.bAccept}")

def print_CZ_PARTY_RECRUIT_ACK_RECALL(v):
  print('Fields of CZ_PARTY_RECRUIT_ACK_RECALL:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_CZ_PARTY_RECRUIT_ADD_FILTERLINGLIST(v):
  print('Fields of CZ_PARTY_RECRUIT_ADD_FILTERLINGLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_CZ_PARTY_RECRUIT_CANCEL_VOLUNTEER(v):
  print('Fields of CZ_PARTY_RECRUIT_CANCEL_VOLUNTEER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_CZ_PARTY_RECRUIT_REFUSE_VOLUNTEER(v):
  print('Fields of CZ_PARTY_RECRUIT_REFUSE_VOLUNTEER:')
  print(f" - packetId: {v.packetId}")
  print(f" - REFUSE_AID: {v.REFUSE_AID}")

def print_CZ_PARTY_RECRUIT_REQ_DELETE(v):
  print('Fields of CZ_PARTY_RECRUIT_REQ_DELETE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_PARTY_RECRUIT_REQ_REGISTER(v):
  print('Fields of CZ_PARTY_RECRUIT_REQ_REGISTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - partyRecruitInfo: {v.partyRecruitInfo}")

def print_CZ_PARTY_RECRUIT_REQ_REGISTER_SUB(v):
  print('Fields of CZ_PARTY_RECRUIT_REQ_REGISTER_SUB:')
  print(f" - Level: {v.Level}")
  print(f" - Notice: {v.Notice}")

def print_CZ_PARTY_RECRUIT_REQ_SEARCH(v):
  print('Fields of CZ_PARTY_RECRUIT_REQ_SEARCH:')
  print(f" - packetId: {v.packetId}")
  print(f" - Level: {v.Level}")
  print(f" - LastIndex: {v.LastIndex}")
  print(f" - ResultCount: {v.ResultCount}")

def print_CZ_PARTY_RECRUIT_REQ_UPDATE(v):
  print('Fields of CZ_PARTY_RECRUIT_REQ_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Notice: {v.Notice}")

def print_CZ_PARTY_RECRUIT_REQ_VOLUNTEER(v):
  print('Fields of CZ_PARTY_RECRUIT_REQ_VOLUNTEER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_CZ_PARTY_RECRUIT_SHOW_EQUIPMENT(v):
  print('Fields of CZ_PARTY_RECRUIT_SHOW_EQUIPMENT:')
  print(f" - packetId: {v.packetId}")
  print(f" - TargetGID: {v.TargetGID}")

def print_CZ_PARTY_RECRUIT_SUB_FILTERLINGLIST(v):
  print('Fields of CZ_PARTY_RECRUIT_SUB_FILTERLINGLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CZ_PC_BUY_CASH_POINT_ITEM(v):
  print('Fields of CZ_PC_BUY_CASH_POINT_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - count: {v.count}")

def print_CZ_PC_PURCHASE_ITEMLIST(v):
  print('Fields of CZ_PC_PURCHASE_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_CZ_PC_PURCHASE_ITEMLIST_FROMMC(v):
  print('Fields of CZ_PC_PURCHASE_ITEMLIST_FROMMC:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - itemInfo: {v.itemInfo}")

def print_CZ_PC_PURCHASE_ITEMLIST_FROMMC2(v):
  print('Fields of CZ_PC_PURCHASE_ITEMLIST_FROMMC2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - UniqueID: {v.UniqueID}")
  print(f" - itemList: {v.itemList}")

def print_CZ_PC_PURCHASE_ITEMLIST_FROMMC2_SUB(v):
  print('Fields of CZ_PC_PURCHASE_ITEMLIST_FROMMC2_SUB:')
  print(f" - count: {v.count}")
  print(f" - index: {v.index}")

def print_CZ_PC_PURCHASE_ITEMLIST_FROMMC_SUB(v):
  print('Fields of CZ_PC_PURCHASE_ITEMLIST_FROMMC_SUB:')
  print(f" - count: {v.count}")
  print(f" - index: {v.index}")

def print_CZ_PC_PURCHASE_ITEMLIST_SUB(v):
  print('Fields of CZ_PC_PURCHASE_ITEMLIST_SUB:')
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")

def print_CZ_PC_SELL_ITEMLIST(v):
  print('Fields of CZ_PC_SELL_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_CZ_PC_SELL_ITEMLIST_SUB(v):
  print('Fields of CZ_PC_SELL_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_PETEGG_INFO(v):
  print('Fields of CZ_PETEGG_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_CZ_PET_ACT(v):
  print('Fields of CZ_PET_ACT:')
  print(f" - packetId: {v.packetId}")
  print(f" - data: {v.data}")

def print_CZ_PET_EVOLUTION(v):
  print('Fields of CZ_PET_EVOLUTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - EvolutionPetEggITID: {v.EvolutionPetEggITID}")

def print_CZ_PKMODE_CHANGE(v):
  print('Fields of CZ_PKMODE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - isTurnOn: {v.isTurnOn}")

def print_CZ_PROGRESS(v):
  print('Fields of CZ_PROGRESS:')
  print(f" - packetId: {v.packetId}")

def print_CZ_RECALL(v):
  print('Fields of CZ_RECALL:')
  print(f" - packetId: {v.packetId}")
  print(f" - AccountName: {v.AccountName}")

def print_CZ_RECALL_GID(v):
  print('Fields of CZ_RECALL_GID:')
  print(f" - packetId: {v.packetId}")
  print(f" - CharacterName: {v.CharacterName}")

def print_CZ_RECALL_SSO(v):
  print('Fields of CZ_RECALL_SSO:')
  print(f" - packetId: {v.packetId}")
  print(f" - aid: {v.aid}")

def print_CZ_RECV_ROULETTE_ITEM(v):
  print('Fields of CZ_RECV_ROULETTE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Condition: {v.Condition}")

def print_CZ_REGISTER_GUILD_EMBLEM_IMG(v):
  print('Fields of CZ_REGISTER_GUILD_EMBLEM_IMG:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - img: {v.img}")

def print_CZ_REG_CHANGE_GUILD_POSITIONINFO(v):
  print('Fields of CZ_REG_CHANGE_GUILD_POSITIONINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - positionInfo: {v.positionInfo}")

def print_CZ_REG_CHANGE_GUILD_POSITIONINFO_SUB(v):
  print('Fields of CZ_REG_CHANGE_GUILD_POSITIONINFO_SUB:')
  print(f" - positionID: {v.positionID}")
  print(f" - right: {v.right}")
  print(f" - ranking: {v.ranking}")
  print(f" - payRate: {v.payRate}")
  print(f" - posName: {v.posName}")

def print_CZ_REMEMBER_WARPPOINT(v):
  print('Fields of CZ_REMEMBER_WARPPOINT:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REMOVE_AID(v):
  print('Fields of CZ_REMOVE_AID:')
  print(f" - packetId: {v.packetId}")
  print(f" - AccountName: {v.AccountName}")

def print_CZ_REMOVE_AID_SSO(v):
  print('Fields of CZ_REMOVE_AID_SSO:')
  print(f" - packetId: {v.packetId}")
  print(f" - aid: {v.aid}")

def print_CZ_RENAME_MER(v):
  print('Fields of CZ_RENAME_MER:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")

def print_CZ_RENAME_PET(v):
  print('Fields of CZ_RENAME_PET:')
  print(f" - packetId: {v.packetId}")
  print(f" - szName: {v.szName}")

def print_CZ_REPLY_ENTRY_QUEUE_ADMISSION(v):
  print('Fields of CZ_REPLY_ENTRY_QUEUE_ADMISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_CZ_REPLY_LOBBY_ADMISSION(v):
  print('Fields of CZ_REPLY_LOBBY_ADMISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - EntryQueueName: {v.EntryQueueName}")
  print(f" - LobbyName: {v.LobbyName}")

def print_CZ_REQMAKINGHOMUN(v):
  print('Fields of CZ_REQMAKINGHOMUN:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_CZ_REQMAKINGITEM(v):
  print('Fields of CZ_REQMAKINGITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - material_ID: {v.material_ID}")

def print_CZ_REQNAME(v):
  print('Fields of CZ_REQNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQNAME2(v):
  print('Fields of CZ_REQNAME2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQNAME_BYGID(v):
  print('Fields of CZ_REQNAME_BYGID:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CZ_REQNAME_BYGID2(v):
  print('Fields of CZ_REQNAME_BYGID2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CZ_REQUEST_ACT(v):
  print('Fields of CZ_REQUEST_ACT:')
  print(f" - packetId: {v.packetId}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - action: {v.action}")

def print_CZ_REQUEST_ACT2(v):
  print('Fields of CZ_REQUEST_ACT2:')
  print(f" - packetId: {v.packetId}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - action: {v.action}")

def print_CZ_REQUEST_ACTNPC(v):
  print('Fields of CZ_REQUEST_ACTNPC:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - action: {v.action}")

def print_CZ_REQUEST_CHAT(v):
  print('Fields of CZ_REQUEST_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_CZ_REQUEST_CHAT_PARTY(v):
  print('Fields of CZ_REQUEST_CHAT_PARTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_CZ_REQUEST_MOVE(v):
  print('Fields of CZ_REQUEST_MOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - dest: {v.dest}")

def print_CZ_REQUEST_MOVE2(v):
  print('Fields of CZ_REQUEST_MOVE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - dest: {v.dest}")

def print_CZ_REQUEST_MOVENPC(v):
  print('Fields of CZ_REQUEST_MOVENPC:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - dest: {v.dest}")

def print_CZ_REQUEST_MOVETOOWNER(v):
  print('Fields of CZ_REQUEST_MOVETOOWNER:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CZ_REQUEST_QUIT(v):
  print('Fields of CZ_REQUEST_QUIT:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQUEST_TIME(v):
  print('Fields of CZ_REQUEST_TIME:')
  print(f" - packetId: {v.packetId}")
  print(f" - clientTime: {v.clientTime}")

def print_CZ_REQUEST_TIME2(v):
  print('Fields of CZ_REQUEST_TIME2:')
  print(f" - packetId: {v.packetId}")
  print(f" - clientTime: {v.clientTime}")

def print_CZ_REQ_ACCOUNTNAME(v):
  print('Fields of CZ_REQ_ACCOUNTNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_ACH_REWARD(v):
  print('Fields of CZ_REQ_ACH_REWARD:')
  print(f" - packetId: {v.packetId}")
  print(f" - ACHID: {v.ACHID}")

def print_CZ_REQ_ADD_ITEM_TO_MAIL(v):
  print('Fields of CZ_REQ_ADD_ITEM_TO_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_CZ_REQ_ALLY_GUILD(v):
  print('Fields of CZ_REQ_ALLY_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - MyAID: {v.MyAID}")
  print(f" - MyGID: {v.MyGID}")

def print_CZ_REQ_APPLY_BARGAIN_SALE_ITEM(v):
  print('Fields of CZ_REQ_APPLY_BARGAIN_SALE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - ItemID: {v.ItemID}")
  print(f" - Count: {v.Count}")
  print(f" - StartDate: {v.StartDate}")
  print(f" - SellingTime: {v.SellingTime}")

def print_CZ_REQ_BANKING_CHECK(v):
  print('Fields of CZ_REQ_BANKING_CHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_BANKING_DEPOSIT(v):
  print('Fields of CZ_REQ_BANKING_DEPOSIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Money: {v.Money}")

def print_CZ_REQ_BANKING_WITHDRAW(v):
  print('Fields of CZ_REQ_BANKING_WITHDRAW:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Money: {v.Money}")

def print_CZ_REQ_BAN_GUILD(v):
  print('Fields of CZ_REQ_BAN_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - reasonDesc: {v.reasonDesc}")

def print_CZ_REQ_BATTLE_STATE_MONITOR(v):
  print('Fields of CZ_REQ_BATTLE_STATE_MONITOR:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")
  print(f" - PowerSwitch: {v.PowerSwitch}")

def print_CZ_REQ_BEFORE_WORLD_INFO(v):
  print('Fields of CZ_REQ_BEFORE_WORLD_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_BUY_FROMMC(v):
  print('Fields of CZ_REQ_BUY_FROMMC:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_CANCEL_WRITE_MAIL(v):
  print('Fields of CZ_REQ_CANCEL_WRITE_MAIL:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_CARTOFF(v):
  print('Fields of CZ_REQ_CARTOFF:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_CASH_BARGAIN_SALE_ITEM_INFO(v):
  print('Fields of CZ_REQ_CASH_BARGAIN_SALE_ITEM_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_CHANGECART(v):
  print('Fields of CZ_REQ_CHANGECART:')
  print(f" - packetId: {v.packetId}")
  print(f" - num: {v.num}")

def print_CZ_REQ_CHANGE_MEMBERPOS(v):
  print('Fields of CZ_REQ_CHANGE_MEMBERPOS:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - memberInfo: {v.memberInfo}")

def print_CZ_REQ_CHANGE_MEMBERPOS_SUB(v):
  print('Fields of CZ_REQ_CHANGE_MEMBERPOS_SUB:')
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - positionID: {v.positionID}")

def print_CZ_REQ_CLICK_TO_BUYING_STORE(v):
  print('Fields of CZ_REQ_CLICK_TO_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - makerAID: {v.makerAID}")

def print_CZ_REQ_CLOSESTORE(v):
  print('Fields of CZ_REQ_CLOSESTORE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_CLOSE_BANKING(v):
  print('Fields of CZ_REQ_CLOSE_BANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_CLOSE_BUYING_STORE(v):
  print('Fields of CZ_REQ_CLOSE_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_CLOSE_GUILD_STORAGE(v):
  print('Fields of CZ_REQ_CLOSE_GUILD_STORAGE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_CLOSE_ROULETTE(v):
  print('Fields of CZ_REQ_CLOSE_ROULETTE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_COUNT_BARGAIN_SALE_ITEM(v):
  print('Fields of CZ_REQ_COUNT_BARGAIN_SALE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - ItemID: {v.ItemID}")

def print_CZ_REQ_DELETE_MAIL(v):
  print('Fields of CZ_REQ_DELETE_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - opentype: {v.opentype}")
  print(f" - MailID: {v.MailID}")

def print_CZ_REQ_DELETE_RELATED_GUILD(v):
  print('Fields of CZ_REQ_DELETE_RELATED_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - OpponentGDID: {v.OpponentGDID}")
  print(f" - Relation: {v.Relation}")

def print_CZ_REQ_DISCONNECT(v):
  print('Fields of CZ_REQ_DISCONNECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_CZ_REQ_DISORGANIZE_GUILD(v):
  print('Fields of CZ_REQ_DISORGANIZE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - key: {v.key}")

def print_CZ_REQ_EMOTION(v):
  print('Fields of CZ_REQ_EMOTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_CZ_REQ_ENTER_ROOM(v):
  print('Fields of CZ_REQ_ENTER_ROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - roomID: {v.roomID}")
  print(f" - passwd: {v.passwd}")

def print_CZ_REQ_ENTRY_QUEUE_APPLY(v):
  print('Fields of CZ_REQ_ENTRY_QUEUE_APPLY:')
  print(f" - packetId: {v.packetId}")
  print(f" - ApplyType: {v.ApplyType}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_CZ_REQ_ENTRY_QUEUE_CANCEL(v):
  print('Fields of CZ_REQ_ENTRY_QUEUE_CANCEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_CZ_REQ_ENTRY_QUEUE_RANKING(v):
  print('Fields of CZ_REQ_ENTRY_QUEUE_RANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_CZ_REQ_EXCHANGE_ITEM(v):
  print('Fields of CZ_REQ_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_EXPEL_GROUP_MEMBER(v):
  print('Fields of CZ_REQ_EXPEL_GROUP_MEMBER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - characterName: {v.characterName}")

def print_CZ_REQ_EXPEL_MEMBER(v):
  print('Fields of CZ_REQ_EXPEL_MEMBER:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")

def print_CZ_REQ_GENERATE_ROULETTE(v):
  print('Fields of CZ_REQ_GENERATE_ROULETTE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_GIVE_MANNER_BYNAME(v):
  print('Fields of CZ_REQ_GIVE_MANNER_BYNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - CharName: {v.CharName}")

def print_CZ_REQ_GIVE_MANNER_POINT(v):
  print('Fields of CZ_REQ_GIVE_MANNER_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - otherAID: {v.otherAID}")
  print(f" - type: {v.type}")
  print(f" - point: {v.point}")

def print_CZ_REQ_GUILDSTORAGE_LOG(v):
  print('Fields of CZ_REQ_GUILDSTORAGE_LOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - RecentIdx: {v.RecentIdx}")

def print_CZ_REQ_GUILD_EMBLEM_IMG(v):
  print('Fields of CZ_REQ_GUILD_EMBLEM_IMG:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")

def print_CZ_REQ_GUILD_MEMBER_INFO(v):
  print('Fields of CZ_REQ_GUILD_MEMBER_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_CZ_REQ_GUILD_MENU(v):
  print('Fields of CZ_REQ_GUILD_MENU:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_CZ_REQ_GUILD_MENUINTERFACE(v):
  print('Fields of CZ_REQ_GUILD_MENUINTERFACE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_GUILD_NAME(v):
  print('Fields of CZ_REQ_GUILD_NAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GuildID: {v.GuildID}")

def print_CZ_REQ_HOSTILE_GUILD(v):
  print('Fields of CZ_REQ_HOSTILE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_ITEMCOMPOSITION(v):
  print('Fields of CZ_REQ_ITEMCOMPOSITION:')
  print(f" - packetId: {v.packetId}")
  print(f" - cardIndex: {v.cardIndex}")
  print(f" - equipIndex: {v.equipIndex}")

def print_CZ_REQ_ITEMCOMPOSITION_LIST(v):
  print('Fields of CZ_REQ_ITEMCOMPOSITION_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - cardIndex: {v.cardIndex}")

def print_CZ_REQ_ITEMIDENTIFY(v):
  print('Fields of CZ_REQ_ITEMIDENTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_CZ_REQ_ITEMREPAIR(v):
  print('Fields of CZ_REQ_ITEMREPAIR:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_CZ_REQ_ITEM_FROM_MAIL(v):
  print('Fields of CZ_REQ_ITEM_FROM_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - opentype: {v.opentype}")

def print_CZ_REQ_JOIN_BABY(v):
  print('Fields of CZ_REQ_JOIN_BABY:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_JOIN_COUPLE(v):
  print('Fields of CZ_REQ_JOIN_COUPLE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_JOIN_GROUP(v):
  print('Fields of CZ_REQ_JOIN_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_JOIN_GUILD(v):
  print('Fields of CZ_REQ_JOIN_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - MyAID: {v.MyAID}")
  print(f" - MyGID: {v.MyGID}")

def print_CZ_REQ_JOIN_GUILD2(v):
  print('Fields of CZ_REQ_JOIN_GUILD2:')
  print(f" - packetId: {v.packetId}")
  print(f" - characterName: {v.characterName}")

def print_CZ_REQ_LEAVE_GROUP(v):
  print('Fields of CZ_REQ_LEAVE_GROUP:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_LEAVE_GUILD(v):
  print('Fields of CZ_REQ_LEAVE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - reasonDesc: {v.reasonDesc}")

def print_CZ_REQ_MAIL_RETURN(v):
  print('Fields of CZ_REQ_MAIL_RETURN:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - ReceiveName: {v.ReceiveName}")

def print_CZ_REQ_MAKE_GUILD(v):
  print('Fields of CZ_REQ_MAKE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - GName: {v.GName}")

def print_CZ_REQ_MAKINGARROW(v):
  print('Fields of CZ_REQ_MAKINGARROW:')
  print(f" - packetId: {v.packetId}")
  print(f" - id: {v.id}")

def print_CZ_REQ_MAKINGITEM(v):
  print('Fields of CZ_REQ_MAKINGITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - mkType: {v.mkType}")
  print(f" - id: {v.id}")

def print_CZ_REQ_NEXT_MAIL_LIST(v):
  print('Fields of CZ_REQ_NEXT_MAIL_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - opentype: {v.opentype}")
  print(f" - Lower_MailID: {v.Lower_MailID}")

def print_CZ_REQ_NEXT_SCRIPT(v):
  print('Fields of CZ_REQ_NEXT_SCRIPT:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_CZ_REQ_OPENSTORE(v):
  print('Fields of CZ_REQ_OPENSTORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - storeName: {v.storeName}")
  print(f" - itemInfo: {v.itemInfo}")

def print_CZ_REQ_OPENSTORE2(v):
  print('Fields of CZ_REQ_OPENSTORE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - storeName: {v.storeName}")
  print(f" - result: {v.result}")
  print(f" - list: {v.list}")

def print_CZ_REQ_OPENSTORE2_SUB(v):
  print('Fields of CZ_REQ_OPENSTORE2_SUB:')
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - Price: {v.Price}")

def print_CZ_REQ_OPENSTORE_SUB(v):
  print('Fields of CZ_REQ_OPENSTORE_SUB:')
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - Price: {v.Price}")

def print_CZ_REQ_OPEN_BANKING(v):
  print('Fields of CZ_REQ_OPEN_BANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_OPEN_BUYING_STORE(v):
  print('Fields of CZ_REQ_OPEN_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - LimitZeny: {v.LimitZeny}")
  print(f" - result: {v.result}")
  print(f" - storeName: {v.storeName}")
  print(f" - itemList: {v.itemList}")

def print_CZ_REQ_OPEN_BUYING_STORE_ITEMLIST(v):
  print('Fields of CZ_REQ_OPEN_BUYING_STORE_ITEMLIST:')
  print(f" - ITID: {v.ITID}")
  print(f" - count: {v.count}")
  print(f" - price: {v.price}")

def print_CZ_REQ_OPEN_GUILD_STORAGE(v):
  print('Fields of CZ_REQ_OPEN_GUILD_STORAGE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_OPEN_MEMBER_INFO(v):
  print('Fields of CZ_REQ_OPEN_MEMBER_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_CZ_REQ_OPEN_ROULETTE(v):
  print('Fields of CZ_REQ_OPEN_ROULETTE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_OPEN_WRITE_MAIL(v):
  print('Fields of CZ_REQ_OPEN_WRITE_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - receiveName: {v.receiveName}")

def print_CZ_REQ_PARTY_NAME(v):
  print('Fields of CZ_REQ_PARTY_NAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - PartyID: {v.PartyID}")

def print_CZ_REQ_PVPPOINT(v):
  print('Fields of CZ_REQ_PVPPOINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")

def print_CZ_REQ_RANKING(v):
  print('Fields of CZ_REQ_RANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - RankingType: {v.RankingType}")

def print_CZ_REQ_READ_MAIL(v):
  print('Fields of CZ_REQ_READ_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - opentype: {v.opentype}")
  print(f" - MailID: {v.MailID}")

def print_CZ_REQ_REFRESH_MAIL_LIST(v):
  print('Fields of CZ_REQ_REFRESH_MAIL_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - opentype: {v.opentype}")
  print(f" - Upper_MailID: {v.Upper_MailID}")

def print_CZ_REQ_REMAINTIME(v):
  print('Fields of CZ_REQ_REMAINTIME:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_REMOVE_BARGAIN_SALE_ITEM(v):
  print('Fields of CZ_REQ_REMOVE_BARGAIN_SALE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - ItemID: {v.ItemID}")

def print_CZ_REQ_REMOVE_ITEM_MAIL(v):
  print('Fields of CZ_REQ_REMOVE_ITEM_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - cnt: {v.cnt}")

def print_CZ_REQ_ROLE_CHANGE(v):
  print('Fields of CZ_REQ_ROLE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - role: {v.role}")
  print(f" - name: {v.name}")

def print_CZ_REQ_ROULETTE_INFO(v):
  print('Fields of CZ_REQ_ROULETTE_INFO:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_SCHEDULER_CASHITEM(v):
  print('Fields of CZ_REQ_SCHEDULER_CASHITEM:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_SE_CASH_TAB_CODE(v):
  print('Fields of CZ_REQ_SE_CASH_TAB_CODE:')
  print(f" - packetId: {v.packetId}")
  print(f" - tab_code: {v.tab_code}")

def print_CZ_REQ_STATUS(v):
  print('Fields of CZ_REQ_STATUS:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_STATUS_GM(v):
  print('Fields of CZ_REQ_STATUS_GM:')
  print(f" - packetId: {v.packetId}")
  print(f" - CharName: {v.CharName}")

def print_CZ_REQ_TAKEOFF_EQUIP(v):
  print('Fields of CZ_REQ_TAKEOFF_EQUIP:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_CZ_REQ_TRADE_BUYING_STORE(v):
  print('Fields of CZ_REQ_TRADE_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - makerAID: {v.makerAID}")
  print(f" - StoreID: {v.StoreID}")
  print(f" - itemList: {v.itemList}")

def print_CZ_REQ_TRADE_BUYING_STORE_ITEMLIST(v):
  print('Fields of CZ_REQ_TRADE_BUYING_STORE_ITEMLIST:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - count: {v.count}")

def print_CZ_REQ_USER_COUNT(v):
  print('Fields of CZ_REQ_USER_COUNT:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_WEAPONREFINE(v):
  print('Fields of CZ_REQ_WEAPONREFINE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_CZ_REQ_WEAR_EQUIP(v):
  print('Fields of CZ_REQ_WEAR_EQUIP:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")

def print_CZ_REQ_WEAR_EQUIP_V5(v):
  print('Fields of CZ_REQ_WEAR_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")

def print_CZ_REQ_WHISPER_LIST(v):
  print('Fields of CZ_REQ_WHISPER_LIST:')
  print(f" - packetId: {v.packetId}")

def print_CZ_REQ_WRITE_MAIL(v):
  print('Fields of CZ_REQ_WRITE_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - receiveName: {v.receiveName}")
  print(f" - senderName: {v.senderName}")
  print(f" - zeny: {v.zeny}")
  print(f" - Titlelength: {v.Titlelength}")
  print(f" - TextcontentsLength: {v.TextcontentsLength}")

def print_CZ_REQ_ZENY_FROM_MAIL(v):
  print('Fields of CZ_REQ_ZENY_FROM_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - opentype: {v.opentype}")

def print_CZ_RESET(v):
  print('Fields of CZ_RESET:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_CZ_RESTART(v):
  print('Fields of CZ_RESTART:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_CZ_SEARCH_STORE_INFO(v):
  print('Fields of CZ_SEARCH_STORE_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - StoreType: {v.StoreType}")
  print(f" - maxPrice: {v.maxPrice}")
  print(f" - minPrice: {v.minPrice}")
  print(f" - ItemIDListSize: {v.ItemIDListSize}")
  print(f" - CardIDListSize: {v.CardIDListSize}")

def print_CZ_SEARCH_STORE_INFO_NEXT_PAGE(v):
  print('Fields of CZ_SEARCH_STORE_INFO_NEXT_PAGE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_SEEK_PARTY(v):
  print('Fields of CZ_SEEK_PARTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - Option: {v.Option}")

def print_CZ_SEEK_PARTY_MEMBER(v):
  print('Fields of CZ_SEEK_PARTY_MEMBER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Job: {v.Job}")
  print(f" - Level: {v.Level}")
  print(f" - mapName: {v.mapName}")
  print(f" - Option: {v.Option}")

def print_CZ_SELECTAUTOSPELL(v):
  print('Fields of CZ_SELECTAUTOSPELL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")

def print_CZ_SELECTCART(v):
  print('Fields of CZ_SELECTCART:')
  print(f" - packetId: {v.packetId}")
  print(f" - Identity: {v.Identity}")
  print(f" - type: {v.type}")

def print_CZ_SELECT_PETEGG(v):
  print('Fields of CZ_SELECT_PETEGG:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_CZ_SELECT_WARPPOINT(v):
  print('Fields of CZ_SELECT_WARPPOINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - mapName: {v.mapName}")

def print_CZ_SETTING_WHISPER_PC(v):
  print('Fields of CZ_SETTING_WHISPER_PC:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")
  print(f" - type: {v.type}")

def print_CZ_SETTING_WHISPER_STATE(v):
  print('Fields of CZ_SETTING_WHISPER_STATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_CZ_SE_CASHSHOP_CLOSE(v):
  print('Fields of CZ_SE_CASHSHOP_CLOSE:')
  print(f" - packetId: {v.packetId}")

def print_CZ_SE_CASHSHOP_OPEN(v):
  print('Fields of CZ_SE_CASHSHOP_OPEN:')
  print(f" - packetId: {v.packetId}")

def print_CZ_SE_PC_BUY_CASHITEM_LIST(v):
  print('Fields of CZ_SE_PC_BUY_CASHITEM_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - item_count: {v.item_count}")
  print(f" - itemList: {v.itemList}")

def print_CZ_SE_PC_BUY_CASHITEM_LIST_SUB(v):
  print('Fields of CZ_SE_PC_BUY_CASHITEM_LIST_SUB:')
  print(f" - item_id: {v.item_id}")
  print(f" - count: {v.count}")
  print(f" - tab_code: {v.tab_code}")

def print_CZ_SHIFT(v):
  print('Fields of CZ_SHIFT:')
  print(f" - packetId: {v.packetId}")
  print(f" - CharacterName: {v.CharacterName}")

def print_CZ_SHORTCUTKEYBAR_ROTATE(v):
  print('Fields of CZ_SHORTCUTKEYBAR_ROTATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Rotate: {v.Rotate}")

def print_CZ_SHORTCUT_KEY_CHANGE(v):
  print('Fields of CZ_SHORTCUT_KEY_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - isSkill: {v.isSkill}")
  print(f" - ID: {v.ID}")
  print(f" - count: {v.count}")

def print_CZ_SIMPLE_BUY_CASH_POINT_ITEM(v):
  print('Fields of CZ_SIMPLE_BUY_CASH_POINT_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - count: {v.count}")

def print_CZ_SIMPLE_CASH_BTNSHOW(v):
  print('Fields of CZ_SIMPLE_CASH_BTNSHOW:')
  print(f" - packetId: {v.packetId}")

def print_CZ_SKILL_SELECT_RESPONSE(v):
  print('Fields of CZ_SKILL_SELECT_RESPONSE:')
  print(f" - packetId: {v.packetId}")
  print(f" - why: {v.why}")
  print(f" - SKID: {v.SKID}")

def print_CZ_SRPACKETR2_START(v):
  print('Fields of CZ_SRPACKETR2_START:')
  print(f" - packetId: {v.packetId}")
  print(f" - ProtectFactor: {v.ProtectFactor}")

def print_CZ_SSILIST_ITEM_CLICK(v):
  print('Fields of CZ_SSILIST_ITEM_CLICK:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - SSI_ID: {v.SSI_ID}")
  print(f" - ITID: {v.ITID}")

def print_CZ_STANDING_RESURRECTION(v):
  print('Fields of CZ_STANDING_RESURRECTION:')
  print(f" - packetId: {v.packetId}")

def print_CZ_STATUS_CHANGE(v):
  print('Fields of CZ_STATUS_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - statusID: {v.statusID}")
  print(f" - changeAmount: {v.changeAmount}")

def print_CZ_TAEKWON_RANK(v):
  print('Fields of CZ_TAEKWON_RANK:')
  print(f" - packetId: {v.packetId}")

def print_CZ_TRYCAPTURE_MONSTER(v):
  print('Fields of CZ_TRYCAPTURE_MONSTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - targetAID: {v.targetAID}")

def print_CZ_TRYCOLLECTION(v):
  print('Fields of CZ_TRYCOLLECTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - targetAID: {v.targetAID}")

def print_CZ_UPGRADE_SKILLLEVEL(v):
  print('Fields of CZ_UPGRADE_SKILLLEVEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")

def print_CZ_USE_ITEM(v):
  print('Fields of CZ_USE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - AID: {v.AID}")

def print_CZ_USE_ITEM2(v):
  print('Fields of CZ_USE_ITEM2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - AID: {v.AID}")

def print_CZ_USE_SKILL(v):
  print('Fields of CZ_USE_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - targetID: {v.targetID}")

def print_CZ_USE_SKILL2(v):
  print('Fields of CZ_USE_SKILL2:')
  print(f" - packetId: {v.packetId}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - targetID: {v.targetID}")

def print_CZ_USE_SKILL_TOGROUND(v):
  print('Fields of CZ_USE_SKILL_TOGROUND:')
  print(f" - packetId: {v.packetId}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_CZ_USE_SKILL_TOGROUND2(v):
  print('Fields of CZ_USE_SKILL_TOGROUND2:')
  print(f" - packetId: {v.packetId}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_CZ_USE_SKILL_TOGROUND_WITHTALKBOX(v):
  print('Fields of CZ_USE_SKILL_TOGROUND_WITHTALKBOX:')
  print(f" - packetId: {v.packetId}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - contents: {v.contents}")

def print_CZ_USE_SKILL_TOGROUND_WITHTALKBOX2(v):
  print('Fields of CZ_USE_SKILL_TOGROUND_WITHTALKBOX2:')
  print(f" - packetId: {v.packetId}")
  print(f" - selectedLevel: {v.selectedLevel}")
  print(f" - SKID: {v.SKID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - contents: {v.contents}")

def print_CZ_WHISPER(v):
  print('Fields of CZ_WHISPER:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - receiver: {v.receiver}")
  print(f" - msg: {v.msg}")

def print_HC_ACCEPT2(v):
  print('Fields of HC_ACCEPT2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - NormalSlotNum: {v.NormalSlotNum}")
  print(f" - PremiumSlotNum: {v.PremiumSlotNum}")
  print(f" - BillingSlotNum: {v.BillingSlotNum}")
  print(f" - ProducibleSlotNum: {v.ProducibleSlotNum}")
  print(f" - ValidSlotNum: {v.ValidSlotNum}")
  print(f" - m_extension: {v.m_extension}")
  print(f" - charList: {v.charList}")

def print_HC_ACCEPT2_CHARINFO(v):
  print('Fields of HC_ACCEPT2_CHARINFO:')
  print(f" - GID: {v.GID}")
  print(f" - exp: {v.exp}")
  print(f" - money: {v.money}")
  print(f" - jobexp: {v.jobexp}")
  print(f" - joblevel: {v.joblevel}")
  print(f" - bodystate: {v.bodystate}")
  print(f" - healthstate: {v.healthstate}")
  print(f" - effectstate: {v.effectstate}")
  print(f" - virtue: {v.virtue}")
  print(f" - honor: {v.honor}")
  print(f" - jobpoint: {v.jobpoint}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")
  print(f" - sp: {v.sp}")
  print(f" - maxsp: {v.maxsp}")
  print(f" - speed: {v.speed}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - level: {v.level}")
  print(f" - sppoint: {v.sppoint}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - name: {v.name}")
  print(f" - Str: {v.Str}")
  print(f" - Agi: {v.Agi}")
  print(f" - Vit: {v.Vit}")
  print(f" - Int: {v.Int}")
  print(f" - Dex: {v.Dex}")
  print(f" - Luk: {v.Luk}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - haircolor: {v.haircolor}")
  print(f" - bIsChangedCharName: {v.bIsChangedCharName}")
  print(f" - Robe: {v.Robe}")

def print_HC_ACCEPT_DELETECHAR(v):
  print('Fields of HC_ACCEPT_DELETECHAR:')
  print(f" - packetId: {v.packetId}")

def print_HC_ACCEPT_ENTER_NEO_UNION(v):
  print('Fields of HC_ACCEPT_ENTER_NEO_UNION:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - TotalSlotNum: {v.TotalSlotNum}")
  print(f" - PremiumStartSlot: {v.PremiumStartSlot}")
  print(f" - PremiumEndSlot: {v.PremiumEndSlot}")
  print(f" - dummy1_beginbilling: {v.dummy1_beginbilling}")
  print(f" - code: {v.code}")
  print(f" - time1: {v.time1}")
  print(f" - time2: {v.time2}")
  print(f" - dummy2_endbilling: {v.dummy2_endbilling}")
  print(f" - character_list: {v.character_list}")

def print_HC_ACCEPT_ENTER_NEO_UNION_SUB(v):
  print('Fields of HC_ACCEPT_ENTER_NEO_UNION_SUB:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - exp: {v.exp}")
  print(f" - money: {v.money}")
  print(f" - jobexp: {v.jobexp}")
  print(f" - joblevel: {v.joblevel}")
  print(f" - bodystate: {v.bodystate}")
  print(f" - healthstate: {v.healthstate}")
  print(f" - effectstate: {v.effectstate}")
  print(f" - virtue: {v.virtue}")
  print(f" - honor: {v.honor}")
  print(f" - jobpoint: {v.jobpoint}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")
  print(f" - sp: {v.sp}")
  print(f" - maxsp: {v.maxsp}")
  print(f" - speed: {v.speed}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - level: {v.level}")
  print(f" - sppoint: {v.sppoint}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - name: {v.name}")
  print(f" - Str: {v.Str}")
  print(f" - Agi: {v.Agi}")
  print(f" - Vit: {v.Vit}")
  print(f" - Int: {v.Int}")
  print(f" - Dex: {v.Dex}")
  print(f" - Luk: {v.Luk}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - haircolor: {v.haircolor}")
  print(f" - bIsChangedCharName: {v.bIsChangedCharName}")
  print(f" - lastMap: {v.lastMap}")
  print(f" - DeleteDate: {v.DeleteDate}")
  print(f" - Robe: {v.Robe}")
  print(f" - SlotAddon: {v.SlotAddon}")
  print(f" - RenameAddon: {v.RenameAddon}")

def print_HC_ACCEPT_MAKECHAR_NEO_UNION(v):
  print('Fields of HC_ACCEPT_MAKECHAR_NEO_UNION:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - exp: {v.exp}")
  print(f" - money: {v.money}")
  print(f" - jobexp: {v.jobexp}")
  print(f" - joblevel: {v.joblevel}")
  print(f" - bodystate: {v.bodystate}")
  print(f" - healthstate: {v.healthstate}")
  print(f" - effectstate: {v.effectstate}")
  print(f" - virtue: {v.virtue}")
  print(f" - honor: {v.honor}")
  print(f" - jobpoint: {v.jobpoint}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")
  print(f" - sp: {v.sp}")
  print(f" - maxsp: {v.maxsp}")
  print(f" - speed: {v.speed}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - level: {v.level}")
  print(f" - sppoint: {v.sppoint}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - name: {v.name}")
  print(f" - Str: {v.Str}")
  print(f" - Agi: {v.Agi}")
  print(f" - Vit: {v.Vit}")
  print(f" - Int: {v.Int}")
  print(f" - Dex: {v.Dex}")
  print(f" - Luk: {v.Luk}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - haircolor: {v.haircolor}")
  print(f" - bIsChangedCharName: {v.bIsChangedCharName}")

def print_HC_ACK_CHANGE_CHARACTERNAME(v):
  print('Fields of HC_ACK_CHANGE_CHARACTERNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - dwResult: {v.dwResult}")

def print_HC_ACK_CHANGE_CHARACTER_SLOT(v):
  print('Fields of HC_ACK_CHANGE_CHARACTER_SLOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Reason: {v.Reason}")
  print(f" - AfterChrSlotCnt: {v.AfterChrSlotCnt}")

def print_HC_ACK_CHANGE_CHARNAME(v):
  print('Fields of HC_ACK_CHANGE_CHARNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - sResult: {v.sResult}")

def print_HC_ACK_CHARINFO_PER_PAGE(v):
  print('Fields of HC_ACK_CHARINFO_PER_PAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - CharInfo: {v.CharInfo}")

def print_HC_ACK_CHARINFO_PER_PAGE_CHARINFO(v):
  print('Fields of HC_ACK_CHARINFO_PER_PAGE_CHARINFO:')
  print(f" - GID: {v.GID}")
  print(f" - exp: {v.exp}")
  print(f" - money: {v.money}")
  print(f" - jobexp: {v.jobexp}")
  print(f" - joblevel: {v.joblevel}")
  print(f" - bodystate: {v.bodystate}")
  print(f" - healthstate: {v.healthstate}")
  print(f" - effectstate: {v.effectstate}")
  print(f" - virtue: {v.virtue}")
  print(f" - honor: {v.honor}")
  print(f" - jobpoint: {v.jobpoint}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")
  print(f" - sp: {v.sp}")
  print(f" - maxsp: {v.maxsp}")
  print(f" - speed: {v.speed}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - level: {v.level}")
  print(f" - sppoint: {v.sppoint}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - name: {v.name}")
  print(f" - Str: {v.Str}")
  print(f" - Agi: {v.Agi}")
  print(f" - Vit: {v.Vit}")
  print(f" - Int: {v.Int}")
  print(f" - Dex: {v.Dex}")
  print(f" - Luk: {v.Luk}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - haircolor: {v.haircolor}")
  print(f" - bIsChangedCharName: {v.bIsChangedCharName}")
  print(f" - lastMap: {v.lastMap}")
  print(f" - DeleteDate: {v.DeleteDate}")
  print(f" - Robe: {v.Robe}")
  print(f" - SlotAddon: {v.SlotAddon}")
  print(f" - RenameAddon: {v.RenameAddon}")

def print_HC_ACK_IS_VALID_CHARNAME(v):
  print('Fields of HC_ACK_IS_VALID_CHARNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - sResult: {v.sResult}")

def print_HC_AVAILABLE_SECOND_PASSWD(v):
  print('Fields of HC_AVAILABLE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_HC_BLOCK_CHARACTER(v):
  print('Fields of HC_BLOCK_CHARACTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - blockList: {v.blockList}")

def print_HC_CHARACTER_LIST(v):
  print('Fields of HC_CHARACTER_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - characterList: {v.characterList}")

def print_HC_CHARACTER_LIST_SUB(v):
  print('Fields of HC_CHARACTER_LIST_SUB:')
  print(f" - dwGID: {v.dwGID}")
  print(f" - SlotIdx: {v.SlotIdx}")

def print_HC_CHARLIST_NOTIFY(v):
  print('Fields of HC_CHARLIST_NOTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - TotalCnt: {v.TotalCnt}")

def print_HC_CHECKBOT(v):
  print('Fields of HC_CHECKBOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - img: {v.img}")

def print_HC_CHECKBOT_RESULT(v):
  print('Fields of HC_CHECKBOT_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Result: {v.Result}")

def print_HC_DELETE_CHAR3(v):
  print('Fields of HC_DELETE_CHAR3:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - Result: {v.Result}")

def print_HC_DELETE_CHAR3_CANCEL(v):
  print('Fields of HC_DELETE_CHAR3_CANCEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - Result: {v.Result}")

def print_HC_DELETE_CHAR3_RESERVED(v):
  print('Fields of HC_DELETE_CHAR3_RESERVED:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - Result: {v.Result}")
  print(f" - DeleteReservedDate: {v.DeleteReservedDate}")

def print_HC_DELETE_SECOND_PASSWD(v):
  print('Fields of HC_DELETE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_HC_EDIT_SECOND_PASSWD(v):
  print('Fields of HC_EDIT_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_HC_MAKE_SECOND_PASSWD(v):
  print('Fields of HC_MAKE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_HC_NOTIFY_ZONESVR(v):
  print('Fields of HC_NOTIFY_ZONESVR:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - mapName: {v.mapName}")
  print(f" - ip: {v.ip}")
  print(f" - port: {v.port}")

def print_HC_NOT_AVAILABLE_SECOND_PASSWD(v):
  print('Fields of HC_NOT_AVAILABLE_SECOND_PASSWD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - Seed: {v.Seed}")

def print_HC_QUEUE_ORDER(v):
  print('Fields of HC_QUEUE_ORDER:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - m_AID: {v.m_AID}")
  print(f" - m_QueueOrder: {v.m_QueueOrder}")

def print_HC_REFUSE_DELETECHAR(v):
  print('Fields of HC_REFUSE_DELETECHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")

def print_HC_REFUSE_ENTER(v):
  print('Fields of HC_REFUSE_ENTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")

def print_HC_REFUSE_MAKECHAR(v):
  print('Fields of HC_REFUSE_MAKECHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")

def print_HC_REFUSE_SELECTCHAR(v):
  print('Fields of HC_REFUSE_SELECTCHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")

def print_HC_REQUEST_CHARACTER_PASSWORD(v):
  print('Fields of HC_REQUEST_CHARACTER_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - dummyValue: {v.dummyValue}")

def print_HC_SECOND_PASSWD_LOGIN(v):
  print('Fields of HC_SECOND_PASSWD_LOGIN:')
  print(f" - packetId: {v.packetId}")
  print(f" - Seed: {v.Seed}")
  print(f" - AID: {v.AID}")
  print(f" - Result: {v.Result}")

def print_HC_SECOND_PASSWD_REQ(v):
  print('Fields of HC_SECOND_PASSWD_REQ:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Seed: {v.Seed}")

def print_HC_SECRETSCAN_DATA(v):
  print('Fields of HC_SECRETSCAN_DATA:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_HC_UPDATE_CHARINFO(v):
  print('Fields of HC_UPDATE_CHARINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - charInfoList: {v.charInfoList}")

def print_HC_UPDATE_CHARINFO_SUB(v):
  print('Fields of HC_UPDATE_CHARINFO_SUB:')
  print(f" - GID: {v.GID}")
  print(f" - exp: {v.exp}")
  print(f" - money: {v.money}")
  print(f" - jobexp: {v.jobexp}")
  print(f" - joblevel: {v.joblevel}")
  print(f" - bodystate: {v.bodystate}")
  print(f" - healthstate: {v.healthstate}")
  print(f" - effectstate: {v.effectstate}")
  print(f" - virtue: {v.virtue}")
  print(f" - honor: {v.honor}")
  print(f" - jobpoint: {v.jobpoint}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")
  print(f" - sp: {v.sp}")
  print(f" - maxsp: {v.maxsp}")
  print(f" - speed: {v.speed}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - level: {v.level}")
  print(f" - sppoint: {v.sppoint}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - name: {v.name}")
  print(f" - Str: {v.Str}")
  print(f" - Agi: {v.Agi}")
  print(f" - Vit: {v.Vit}")
  print(f" - Int: {v.Int}")
  print(f" - Dex: {v.Dex}")
  print(f" - Luk: {v.Luk}")
  print(f" - CharNum: {v.CharNum}")
  print(f" - haircolor: {v.haircolor}")
  print(f" - bIsChangedCharName: {v.bIsChangedCharName}")
  print(f" - lastMap: {v.lastMap}")
  print(f" - DeleteDate: {v.DeleteDate}")
  print(f" - Robe: {v.Robe}")
  print(f" - SlotAddon: {v.SlotAddon}")
  print(f" - RenameAddon: {v.RenameAddon}")

def print_HC_WAITING_LOGIN(v):
  print('Fields of HC_WAITING_LOGIN:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - CurWaitingNum: {v.CurWaitingNum}")

def print_PING(v):
  print('Fields of PING:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_SC_ACK_ENCRYPTION(v):
  print('Fields of SC_ACK_ENCRYPTION:')
  print(f" - packetId: {v.packetId}")

def print_SC_BILLING_INFO(v):
  print('Fields of SC_BILLING_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - dwAmountRemain: {v.dwAmountRemain}")
  print(f" - dwQuantityRemain: {v.dwQuantityRemain}")
  print(f" - dwReserved1: {v.dwReserved1}")
  print(f" - dwReserved2: {v.dwReserved2}")

def print_SC_LOGIN_ANSWER(v):
  print('Fields of SC_LOGIN_ANSWER:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - SteamProcessTM: {v.SteamProcessTM}")
  print(f" - IRWebProcessTM: {v.IRWebProcessTM}")
  print(f" - AccDBProcessTM: {v.AccDBProcessTM}")
  print(f" - SessionProcessTM: {v.SessionProcessTM}")
  print(f" - TransactionID: {v.TransactionID}")

def print_SC_LOGIN_ANSWER_WITH_ID(v):
  print('Fields of SC_LOGIN_ANSWER_WITH_ID:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - SteamProcessTM: {v.SteamProcessTM}")
  print(f" - IRWebProcessTM: {v.IRWebProcessTM}")
  print(f" - AccDBProcessTM: {v.AccDBProcessTM}")
  print(f" - SessionProcessTM: {v.SessionProcessTM}")
  print(f" - TransactionID: {v.TransactionID}")
  print(f" - ID: {v.ID}")

def print_SC_LOGIN_ERROR(v):
  print('Fields of SC_LOGIN_ERROR:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCategory: {v.ErrorCategory}")
  print(f" - ErrorCode: {v.ErrorCode}")
  print(f" - SteamProcessTM: {v.SteamProcessTM}")
  print(f" - IRWebProcessTM: {v.IRWebProcessTM}")
  print(f" - AccDBProcessTM: {v.AccDBProcessTM}")
  print(f" - SessionProcessTM: {v.SessionProcessTM}")

def print_SC_NOTIFY_BAN(v):
  print('Fields of SC_NOTIFY_BAN:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")

def print_SC_SOCT(v):
  print('Fields of SC_SOCT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_SERVER_ENTRY_ACK(v):
  print('Fields of SERVER_ENTRY_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Header: {v.Header}")
  print(f" - AID: {v.AID}")

def print_ZC_ACCEPT_ENTER(v):
  print('Fields of ZC_ACCEPT_ENTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - startTime: {v.startTime}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")

def print_ZC_ACCEPT_ENTER2(v):
  print('Fields of ZC_ACCEPT_ENTER2:')
  print(f" - packetId: {v.packetId}")
  print(f" - startTime: {v.startTime}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - font: {v.font}")

def print_ZC_ACCEPT_ENTER3(v):
  print('Fields of ZC_ACCEPT_ENTER3:')
  print(f" - packetId: {v.packetId}")
  print(f" - startTime: {v.startTime}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - font: {v.font}")
  print(f" - sex: {v.sex}")

def print_ZC_ACCEPT_QUIT(v):
  print('Fields of ZC_ACCEPT_QUIT:')
  print(f" - packetId: {v.packetId}")

def print_ZC_ACH_UPDATE(v):
  print('Fields of ZC_ACH_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - ACHPoint: {v.ACHPoint}")
  print(f" - ACHID: {v.ACHID}")
  print(f" - bComplete: {v.bComplete}")
  print(f" - count1: {v.count1}")
  print(f" - count2: {v.count2}")
  print(f" - count3: {v.count3}")
  print(f" - count4: {v.count4}")
  print(f" - count5: {v.count5}")
  print(f" - completeDate: {v.completeDate}")
  print(f" - bGetReward: {v.bGetReward}")

def print_ZC_ACK_ACCOUNTNAME(v):
  print('Fields of ZC_ACK_ACCOUNTNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - name: {v.name}")

def print_ZC_ACK_ADDITEM_TO_CART(v):
  print('Fields of ZC_ACK_ADDITEM_TO_CART:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_ADD_EXCHANGE_ITEM(v):
  print('Fields of ZC_ACK_ADD_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - result: {v.result}")

def print_ZC_ACK_ADD_ITEM_TO_MAIL(v):
  print('Fields of ZC_ACK_ADD_ITEM_TO_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketType: {v.PacketType}")
  print(f" - result: {v.result}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")
  print(f" - weight: {v.weight}")

def print_ZC_ACK_APPLY_BARGAIN_SALE_ITEM(v):
  print('Fields of ZC_ACK_APPLY_BARGAIN_SALE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_AUCTION_ADD_ITEM(v):
  print('Fields of ZC_ACK_AUCTION_ADD_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - result: {v.result}")

def print_ZC_ACK_BANKING_DEPOSIT(v):
  print('Fields of ZC_ACK_BANKING_DEPOSIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Reason: {v.Reason}")
  print(f" - Money: {v.Money}")

def print_ZC_ACK_BANKING_WITHDRAW(v):
  print('Fields of ZC_ACK_BANKING_WITHDRAW:')
  print(f" - packetId: {v.packetId}")
  print(f" - Reason: {v.Reason}")
  print(f" - Money: {v.Money}")

def print_ZC_ACK_BAN_GUILD(v):
  print('Fields of ZC_ACK_BAN_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - charName: {v.charName}")
  print(f" - reasonDesc: {v.reasonDesc}")
  print(f" - account: {v.account}")

def print_ZC_ACK_BAN_GUILD_SSO(v):
  print('Fields of ZC_ACK_BAN_GUILD_SSO:')
  print(f" - packetId: {v.packetId}")
  print(f" - charName: {v.charName}")
  print(f" - reasonDesc: {v.reasonDesc}")

def print_ZC_ACK_BATTLE_STATE_MONITOR(v):
  print('Fields of ZC_ACK_BATTLE_STATE_MONITOR:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")
  print(f" - PlayCount: {v.PlayCount}")
  print(f" - BattleState: {v.BattleState}")
  print(f" - TeamCount_A: {v.TeamCount_A}")
  print(f" - TeamCount_B: {v.TeamCount_B}")
  print(f" - MyCount: {v.MyCount}")
  print(f" - JoinTeam: {v.JoinTeam}")

def print_ZC_ACK_BEFORE_WORLD_INFO(v):
  print('Fields of ZC_ACK_BEFORE_WORLD_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - WorldName: {v.WorldName}")
  print(f" - CharName: {v.CharName}")

def print_ZC_ACK_CASH_BARGAIN_SALE_ITEM_INFO(v):
  print('Fields of ZC_ACK_CASH_BARGAIN_SALE_ITEM_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - ItemID: {v.ItemID}")
  print(f" - Price: {v.Price}")

def print_ZC_ACK_CHANGE_GUILD_POSITIONINFO(v):
  print('Fields of ZC_ACK_CHANGE_GUILD_POSITIONINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - positionInfo: {v.positionInfo}")

def print_ZC_ACK_CHANGE_GUILD_POSITIONINFO_SUB(v):
  print('Fields of ZC_ACK_CHANGE_GUILD_POSITIONINFO_SUB:')
  print(f" - positionID: {v.positionID}")
  print(f" - right: {v.right}")
  print(f" - ranking: {v.ranking}")
  print(f" - payRate: {v.payRate}")
  print(f" - posName: {v.posName}")

def print_ZC_ACK_CLAN_LEAVE(v):
  print('Fields of ZC_ACK_CLAN_LEAVE:')
  print(f" - packetId: {v.packetId}")

def print_ZC_ACK_CLOSE_BANKING(v):
  print('Fields of ZC_ACK_CLOSE_BANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_CLOSE_GUILD_STORAGE(v):
  print('Fields of ZC_ACK_CLOSE_GUILD_STORAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_CLOSE_ROULETTE(v):
  print('Fields of ZC_ACK_CLOSE_ROULETTE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_COUNT_BARGAIN_SALE_ITEM(v):
  print('Fields of ZC_ACK_COUNT_BARGAIN_SALE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - ItemID: {v.ItemID}")
  print(f" - RemainCount: {v.RemainCount}")

def print_ZC_ACK_CREATE_CHATROOM(v):
  print('Fields of ZC_ACK_CREATE_CHATROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_DELETE_MAIL(v):
  print('Fields of ZC_ACK_DELETE_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - opentype: {v.opentype}")
  print(f" - MailID: {v.MailID}")

def print_ZC_ACK_DISCONNECT_CHARACTER(v):
  print('Fields of ZC_ACK_DISCONNECT_CHARACTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_DISORGANIZE_GUILD(v):
  print('Fields of ZC_ACK_DISORGANIZE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - reasonDesc: {v.reasonDesc}")

def print_ZC_ACK_DISORGANIZE_GUILD_RESULT(v):
  print('Fields of ZC_ACK_DISORGANIZE_GUILD_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - reason: {v.reason}")

def print_ZC_ACK_ENTRY_QUEUE_APPLY(v):
  print('Fields of ZC_ACK_ENTRY_QUEUE_APPLY:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_ZC_ACK_ENTRY_QUEUE_CANCEL(v):
  print('Fields of ZC_ACK_ENTRY_QUEUE_CANCEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_ZC_ACK_EXCHANGE_ITEM(v):
  print('Fields of ZC_ACK_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_EXCHANGE_ITEM2(v):
  print('Fields of ZC_ACK_EXCHANGE_ITEM2:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")
  print(f" - GID: {v.GID}")
  print(f" - level: {v.level}")

def print_ZC_ACK_GENERATE_ROULETTE(v):
  print('Fields of ZC_ACK_GENERATE_ROULETTE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - Step: {v.Step}")
  print(f" - Idx: {v.Idx}")
  print(f" - AdditionItemID: {v.AdditionItemID}")
  print(f" - RemainGold: {v.RemainGold}")
  print(f" - RemainSilver: {v.RemainSilver}")
  print(f" - RemainBronze: {v.RemainBronze}")

def print_ZC_ACK_GIVE_MANNER_POINT(v):
  print('Fields of ZC_ACK_GIVE_MANNER_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_GUILDSTORAGE_LOG(v):
  print('Fields of ZC_ACK_GUILDSTORAGE_LOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Result: {v.Result}")
  print(f" - Cnt: {v.Cnt}")

def print_ZC_ACK_GUILD_MEMBER_INFO(v):
  print('Fields of ZC_ACK_GUILD_MEMBER_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - head: {v.head}")
  print(f" - headPalette: {v.headPalette}")
  print(f" - sex: {v.sex}")
  print(f" - job: {v.job}")
  print(f" - level: {v.level}")
  print(f" - contributionExp: {v.contributionExp}")
  print(f" - currentState: {v.currentState}")
  print(f" - positionID: {v.positionID}")
  print(f" - intro: {v.intro}")
  print(f" - charname: {v.charname}")

def print_ZC_ACK_GUILD_MENUINTERFACE(v):
  print('Fields of ZC_ACK_GUILD_MENUINTERFACE:')
  print(f" - packetId: {v.packetId}")
  print(f" - guildMemuFlag: {v.guildMemuFlag}")

def print_ZC_ACK_ITEMCOMPOSITION(v):
  print('Fields of ZC_ACK_ITEMCOMPOSITION:')
  print(f" - packetId: {v.packetId}")
  print(f" - equipIndex: {v.equipIndex}")
  print(f" - cardIndex: {v.cardIndex}")
  print(f" - result: {v.result}")

def print_ZC_ACK_ITEMIDENTIFY(v):
  print('Fields of ZC_ACK_ITEMIDENTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - result: {v.result}")

def print_ZC_ACK_ITEMLIST_BUYING_STORE(v):
  print('Fields of ZC_ACK_ITEMLIST_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - makerAID: {v.makerAID}")
  print(f" - StoreID: {v.StoreID}")
  print(f" - limitZeny: {v.limitZeny}")
  print(f" - itemList: {v.itemList}")

def print_ZC_ACK_ITEMLIST_BUYING_STORE_ITEMLIST(v):
  print('Fields of ZC_ACK_ITEMLIST_BUYING_STORE_ITEMLIST:')
  print(f" - price: {v.price}")
  print(f" - count: {v.count}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")

def print_ZC_ACK_ITEMREFINING(v):
  print('Fields of ZC_ACK_ITEMREFINING:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")
  print(f" - itemIndex: {v.itemIndex}")
  print(f" - refiningLevel: {v.refiningLevel}")

def print_ZC_ACK_ITEMREPAIR(v):
  print('Fields of ZC_ACK_ITEMREPAIR:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - result: {v.result}")

def print_ZC_ACK_ITEM_FROM_MAIL(v):
  print('Fields of ZC_ACK_ITEM_FROM_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - opentype: {v.opentype}")
  print(f" - result: {v.result}")

def print_ZC_ACK_LEAVE_GUILD(v):
  print('Fields of ZC_ACK_LEAVE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - charName: {v.charName}")
  print(f" - reasonDesc: {v.reasonDesc}")

def print_ZC_ACK_MAIL_ADD_ITEM(v):
  print('Fields of ZC_ACK_MAIL_ADD_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - result: {v.result}")

def print_ZC_ACK_MAIL_DELETE(v):
  print('Fields of ZC_ACK_MAIL_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_MAIL_LIST(v):
  print('Fields of ZC_ACK_MAIL_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - opentype: {v.opentype}")
  print(f" - cnt: {v.cnt}")
  print(f" - IsEnd: {v.IsEnd}")

def print_ZC_ACK_MAIL_RETURN(v):
  print('Fields of ZC_ACK_MAIL_RETURN:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_MAKE_GROUP(v):
  print('Fields of ZC_ACK_MAKE_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_MERGE_ITEM(v):
  print('Fields of ZC_ACK_MERGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - item_index: {v.item_index}")
  print(f" - item_count: {v.item_count}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_OPENSTORE2(v):
  print('Fields of ZC_ACK_OPENSTORE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_OPEN_BANKING(v):
  print('Fields of ZC_ACK_OPEN_BANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_OPEN_GUILD_STORAGE(v):
  print('Fields of ZC_ACK_OPEN_GUILD_STORAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - Permission: {v.Permission}")

def print_ZC_ACK_OPEN_MEMBER_INFO(v):
  print('Fields of ZC_ACK_OPEN_MEMBER_INFO:')
  print(f" - packetId: {v.packetId}")

def print_ZC_ACK_OPEN_ROULETTE(v):
  print('Fields of ZC_ACK_OPEN_ROULETTE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - Serial: {v.Serial}")
  print(f" - Step: {v.Step}")
  print(f" - Idx: {v.Idx}")
  print(f" - AdditionItemID: {v.AdditionItemID}")
  print(f" - GoldPoint: {v.GoldPoint}")
  print(f" - SilverPoint: {v.SilverPoint}")
  print(f" - BronzePoint: {v.BronzePoint}")

def print_ZC_ACK_OPEN_WRITE_MAIL(v):
  print('Fields of ZC_ACK_OPEN_WRITE_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - receiveName: {v.receiveName}")
  print(f" - result: {v.result}")

def print_ZC_ACK_PARTY_NAME(v):
  print('Fields of ZC_ACK_PARTY_NAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - PartyID: {v.PartyID}")
  print(f" - szPartyName: {v.szPartyName}")

def print_ZC_ACK_PVPPOINT(v):
  print('Fields of ZC_ACK_PVPPOINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - WinPoint: {v.WinPoint}")
  print(f" - LosePoint: {v.LosePoint}")
  print(f" - Point: {v.Point}")

def print_ZC_ACK_RANKING(v):
  print('Fields of ZC_ACK_RANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - RankingType: {v.RankingType}")
  print(f" - CharName: {v.CharName}")
  print(f" - Point: {v.Point}")
  print(f" - myPoint: {v.myPoint}")

def print_ZC_ACK_READ_MAIL(v):
  print('Fields of ZC_ACK_READ_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - opentype: {v.opentype}")
  print(f" - MailID: {v.MailID}")
  print(f" - TextcontentsLength: {v.TextcontentsLength}")
  print(f" - zeny: {v.zeny}")
  print(f" - ItemCnt: {v.ItemCnt}")

def print_ZC_ACK_REMEMBER_WARPPOINT(v):
  print('Fields of ZC_ACK_REMEMBER_WARPPOINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_ZC_ACK_REMOVE_BARGAIN_SALE_ITEM(v):
  print('Fields of ZC_ACK_REMOVE_BARGAIN_SALE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ACK_REMOVE_ITEM_MAIL(v):
  print('Fields of ZC_ACK_REMOVE_ITEM_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")
  print(f" - index: {v.index}")
  print(f" - cnt: {v.cnt}")
  print(f" - weight: {v.weight}")

def print_ZC_ACK_REQMAKINGITEM(v):
  print('Fields of ZC_ACK_REQMAKINGITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")
  print(f" - ITID: {v.ITID}")

def print_ZC_ACK_REQNAME(v):
  print('Fields of ZC_ACK_REQNAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - CName: {v.CName}")

def print_ZC_ACK_REQNAMEALL(v):
  print('Fields of ZC_ACK_REQNAMEALL:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - CName: {v.CName}")
  print(f" - PName: {v.PName}")
  print(f" - GName: {v.GName}")
  print(f" - RName: {v.RName}")

def print_ZC_ACK_REQNAME_BYGID(v):
  print('Fields of ZC_ACK_REQNAME_BYGID:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - CName: {v.CName}")

def print_ZC_ACK_REQ_ALLY_GUILD(v):
  print('Fields of ZC_ACK_REQ_ALLY_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - answer: {v.answer}")

def print_ZC_ACK_REQ_CHANGE_MEMBERS(v):
  print('Fields of ZC_ACK_REQ_CHANGE_MEMBERS:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - memberInfo: {v.memberInfo}")

def print_ZC_ACK_REQ_CHANGE_MEMBERS_SUB(v):
  print('Fields of ZC_ACK_REQ_CHANGE_MEMBERS_SUB:')
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - positionID: {v.positionID}")

def print_ZC_ACK_REQ_DISCONNECT(v):
  print('Fields of ZC_ACK_REQ_DISCONNECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_REQ_HOSTILE_GUILD(v):
  print('Fields of ZC_ACK_REQ_HOSTILE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_REQ_JOIN_GROUP(v):
  print('Fields of ZC_ACK_REQ_JOIN_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - characterName: {v.characterName}")
  print(f" - answer: {v.answer}")

def print_ZC_ACK_REQ_JOIN_GUILD(v):
  print('Fields of ZC_ACK_REQ_JOIN_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - answer: {v.answer}")

def print_ZC_ACK_ROULEITTE_INFO(v):
  print('Fields of ZC_ACK_ROULEITTE_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - RouletteSerial: {v.RouletteSerial}")

def print_ZC_ACK_SE_CASH_ITEM_LIST(v):
  print('Fields of ZC_ACK_SE_CASH_ITEM_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - item_count: {v.item_count}")
  print(f" - itemList: {v.itemList}")

def print_ZC_ACK_SE_CASH_ITEM_LIST2(v):
  print('Fields of ZC_ACK_SE_CASH_ITEM_LIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - OpenIdentity: {v.OpenIdentity}")
  print(f" - item_count: {v.item_count}")
  print(f" - item_list: {v.item_list}")

def print_ZC_ACK_SE_CASH_ITEM_LIST2_SUB(v):
  print('Fields of ZC_ACK_SE_CASH_ITEM_LIST2_SUB:')
  print(f" - item_id: {v.item_id}")
  print(f" - price: {v.price}")

def print_ZC_ACK_SE_CASH_ITEM_LIST_SUB(v):
  print('Fields of ZC_ACK_SE_CASH_ITEM_LIST_SUB:')
  print(f" - item_id: {v.item_id}")
  print(f" - price: {v.price}")

def print_ZC_ACK_STATUS_GM(v):
  print('Fields of ZC_ACK_STATUS_GM:')
  print(f" - packetId: {v.packetId}")
  print(f" - str: {v.str}")
  print(f" - standardStr: {v.standardStr}")
  print(f" - agi: {v.agi}")
  print(f" - standardAgi: {v.standardAgi}")
  print(f" - vit: {v.vit}")
  print(f" - standardVit: {v.standardVit}")
  print(f" - Int: {v.Int}")
  print(f" - standardInt: {v.standardInt}")
  print(f" - dex: {v.dex}")
  print(f" - standardDex: {v.standardDex}")
  print(f" - luk: {v.luk}")
  print(f" - standardLuk: {v.standardLuk}")
  print(f" - attPower: {v.attPower}")
  print(f" - refiningPower: {v.refiningPower}")
  print(f" - max_mattPower: {v.max_mattPower}")
  print(f" - min_mattPower: {v.min_mattPower}")
  print(f" - itemdefPower: {v.itemdefPower}")
  print(f" - plusdefPower: {v.plusdefPower}")
  print(f" - mdefPower: {v.mdefPower}")
  print(f" - plusmdefPower: {v.plusmdefPower}")
  print(f" - hitSuccessValue: {v.hitSuccessValue}")
  print(f" - avoidSuccessValue: {v.avoidSuccessValue}")
  print(f" - plusAvoidSuccessValue: {v.plusAvoidSuccessValue}")
  print(f" - criticalSuccessValue: {v.criticalSuccessValue}")
  print(f" - ASPD: {v.ASPD}")
  print(f" - plusASPD: {v.plusASPD}")

def print_ZC_ACK_TAKEOFF_EQUIP_V5(v):
  print('Fields of ZC_ACK_TAKEOFF_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - result: {v.result}")

def print_ZC_ACK_TOUSESKILL(v):
  print('Fields of ZC_ACK_TOUSESKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - NUM: {v.NUM}")
  print(f" - result: {v.result}")
  print(f" - cause: {v.cause}")

def print_ZC_ACK_WEAPONREFINE(v):
  print('Fields of ZC_ACK_WEAPONREFINE:')
  print(f" - packetId: {v.packetId}")
  print(f" - msg: {v.msg}")
  print(f" - ITID: {v.ITID}")

def print_ZC_ACK_WEAR_EQUIP_V5(v):
  print('Fields of ZC_ACK_WEAR_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - result: {v.result}")

def print_ZC_ACK_WHISPER(v):
  print('Fields of ZC_ACK_WHISPER:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_WHISPER02(v):
  print('Fields of ZC_ACK_WHISPER02:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")
  print(f" - ReceiverGID: {v.ReceiverGID}")

def print_ZC_ACK_WRITE_MAIL(v):
  print('Fields of ZC_ACK_WRITE_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_ACK_ZENY_FROM_MAIL(v):
  print('Fields of ZC_ACK_ZENY_FROM_MAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - opentype: {v.opentype}")
  print(f" - result: {v.result}")

def print_ZC_ACTION_FAILURE(v):
  print('Fields of ZC_ACTION_FAILURE:')
  print(f" - packetId: {v.packetId}")
  print(f" - errorCode: {v.errorCode}")

def print_ZC_ACTIVE_QUEST(v):
  print('Fields of ZC_ACTIVE_QUEST:')
  print(f" - packetId: {v.packetId}")
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")

def print_ZC_ADD_EXCHANGE_ITEM(v):
  print('Fields of ZC_ADD_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_ADD_EXCHANGE_ITEM2(v):
  print('Fields of ZC_ADD_EXCHANGE_ITEM2:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - count: {v.count}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_ADD_EXCHANGE_ITEM3(v):
  print('Fields of ZC_ADD_EXCHANGE_ITEM3:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - count: {v.count}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")

def print_ZC_ADD_FRIENDS_LIST(v):
  print('Fields of ZC_ADD_FRIENDS_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - Name: {v.Name}")

def print_ZC_ADD_ITEM_TO_CART(v):
  print('Fields of ZC_ADD_ITEM_TO_CART:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_ADD_ITEM_TO_CART2(v):
  print('Fields of ZC_ADD_ITEM_TO_CART2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_ADD_ITEM_TO_CART3(v):
  print('Fields of ZC_ADD_ITEM_TO_CART3:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")

def print_ZC_ADD_ITEM_TO_STORE(v):
  print('Fields of ZC_ADD_ITEM_TO_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_ADD_ITEM_TO_STORE2(v):
  print('Fields of ZC_ADD_ITEM_TO_STORE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_ADD_ITEM_TO_STORE3(v):
  print('Fields of ZC_ADD_ITEM_TO_STORE3:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")

def print_ZC_ADD_MEMBER_TO_GROUP(v):
  print('Fields of ZC_ADD_MEMBER_TO_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Role: {v.Role}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - state: {v.state}")
  print(f" - groupName: {v.groupName}")
  print(f" - characterName: {v.characterName}")
  print(f" - mapName: {v.mapName}")

def print_ZC_ADD_MEMBER_TO_GROUP2(v):
  print('Fields of ZC_ADD_MEMBER_TO_GROUP2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Role: {v.Role}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - state: {v.state}")
  print(f" - groupName: {v.groupName}")
  print(f" - characterName: {v.characterName}")
  print(f" - mapName: {v.mapName}")
  print(f" - ItemPickupRule: {v.ItemPickupRule}")
  print(f" - ItemDivisionRule: {v.ItemDivisionRule}")

def print_ZC_ADD_QUEST(v):
  print('Fields of ZC_ADD_QUEST:')
  print(f" - packetId: {v.packetId}")
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")
  print(f" - quest_svrTime: {v.quest_svrTime}")
  print(f" - quest_endTime: {v.quest_endTime}")
  print(f" - count: {v.count}")
  print(f" - mobList: {v.mobList}")

def print_ZC_ADD_QUEST_EX(v):
  print('Fields of ZC_ADD_QUEST_EX:')
  print(f" - packetId: {v.packetId}")
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")
  print(f" - quest_svrTime: {v.quest_svrTime}")
  print(f" - quest_endTime: {v.quest_endTime}")
  print(f" - count: {v.count}")
  print(f" - QuestList: {v.QuestList}")

def print_ZC_ADD_QUEST_EX_SUB(v):
  print('Fields of ZC_ADD_QUEST_EX_SUB:')
  print(f" - mobGID: {v.mobGID}")
  print(f" - huntCount: {v.huntCount}")
  print(f" - mobName: {v.mobName}")

def print_ZC_ADD_QUEST_SUB(v):
  print('Fields of ZC_ADD_QUEST_SUB:')
  print(f" - mobGID: {v.mobGID}")
  print(f" - huntCount: {v.huntCount}")
  print(f" - mobName: {v.mobName}")

def print_ZC_ADD_RELATED_GUILD(v):
  print('Fields of ZC_ADD_RELATED_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - relation: {v.relation}")
  print(f" - GDID: {v.GDID}")
  print(f" - guildname: {v.guildname}")

def print_ZC_ADD_SKILL(v):
  print('Fields of ZC_ADD_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - type: {v.type}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - skillName: {v.skillName}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_AID(v):
  print('Fields of ZC_AID:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_ALCHEMIST_POINT(v):
  print('Fields of ZC_ALCHEMIST_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Point: {v.Point}")
  print(f" - TotalPoint: {v.TotalPoint}")

def print_ZC_ALCHEMIST_RANK(v):
  print('Fields of ZC_ALCHEMIST_RANK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Name: {v.Name}")
  print(f" - Point: {v.Point}")

def print_ZC_ALL_ACH_LIST(v):
  print('Fields of ZC_ALL_ACH_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ACHCount: {v.ACHCount}")
  print(f" - ACHPoint: {v.ACHPoint}")
  print(f" - ACHList: {v.ACHList}")

def print_ZC_ALL_ACH_LIST_ACH(v):
  print('Fields of ZC_ALL_ACH_LIST_ACH:')
  print(f" - ACHID: {v.ACHID}")
  print(f" - bComplete: {v.bComplete}")
  print(f" - count1: {v.count1}")
  print(f" - count2: {v.count2}")
  print(f" - count3: {v.count3}")
  print(f" - count4: {v.count4}")
  print(f" - count5: {v.count5}")
  print(f" - completeDate: {v.completeDate}")
  print(f" - bGetReward: {v.bGetReward}")

def print_ZC_ALL_QUEST_LIST(v):
  print('Fields of ZC_ALL_QUEST_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - questCount: {v.questCount}")
  print(f" - questList: {v.questList}")

def print_ZC_ALL_QUEST_LIST2(v):
  print('Fields of ZC_ALL_QUEST_LIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - QuestCount: {v.QuestCount}")
  print(f" - questList: {v.questList}")

def print_ZC_ALL_QUEST_LIST2_SUB(v):
  print('Fields of ZC_ALL_QUEST_LIST2_SUB:')
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")
  print(f" - quest_svrTime: {v.quest_svrTime}")
  print(f" - quest_endTime: {v.quest_endTime}")
  print(f" - hunting_count: {v.hunting_count}")

def print_ZC_ALL_QUEST_LIST3(v):
  print('Fields of ZC_ALL_QUEST_LIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - QuestCount: {v.QuestCount}")
  print(f" - QuestList: {v.QuestList}")

def print_ZC_ALL_QUEST_LIST3_SUB(v):
  print('Fields of ZC_ALL_QUEST_LIST3_SUB:')
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")
  print(f" - quest_svrTime: {v.quest_svrTime}")
  print(f" - quest_endTime: {v.quest_endTime}")
  print(f" - hunting_count: {v.hunting_count}")

def print_ZC_ALL_QUEST_LIST_SUB(v):
  print('Fields of ZC_ALL_QUEST_LIST_SUB:')
  print(f" - questID: {v.questID}")
  print(f" - active: {v.active}")

def print_ZC_ALL_QUEST_MISSION(v):
  print('Fields of ZC_ALL_QUEST_MISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - count: {v.count}")
  print(f" - questList: {v.questList}")

def print_ZC_ALL_QUEST_MISSION_MOBS_SUB(v):
  print('Fields of ZC_ALL_QUEST_MISSION_MOBS_SUB:')
  print(f" - mobGID: {v.mobGID}")
  print(f" - huntCount: {v.huntCount}")
  print(f" - mobName: {v.mobName}")

def print_ZC_ALL_QUEST_MISSION_SUB(v):
  print('Fields of ZC_ALL_QUEST_MISSION_SUB:')
  print(f" - questID: {v.questID}")
  print(f" - quest_svrTime: {v.quest_svrTime}")
  print(f" - quest_endTime: {v.quest_endTime}")
  print(f" - count: {v.count}")
  print(f" - mobList: {v.mobList}")

def print_ZC_ATTACK_FAILURE_FOR_DISTANCE(v):
  print('Fields of ZC_ATTACK_FAILURE_FOR_DISTANCE:')
  print(f" - packetId: {v.packetId}")
  print(f" - targetAID: {v.targetAID}")
  print(f" - targetXPos: {v.targetXPos}")
  print(f" - targetYPos: {v.targetYPos}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - currentAttRange: {v.currentAttRange}")

def print_ZC_ATTACK_RANGE(v):
  print('Fields of ZC_ATTACK_RANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - currentAttRange: {v.currentAttRange}")

def print_ZC_AUCTION_ACK_MY_SELL_STOP(v):
  print('Fields of ZC_AUCTION_ACK_MY_SELL_STOP:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_AUCTION_ITEM_REQ_SEARCH(v):
  print('Fields of ZC_AUCTION_ITEM_REQ_SEARCH:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - MaxPage: {v.MaxPage}")
  print(f" - Number: {v.Number}")
  print(f" - auctions: {v.auctions}")

def print_ZC_AUCTION_ITEM_REQ_SEARCH_SUB(v):
  print('Fields of ZC_AUCTION_ITEM_REQ_SEARCH_SUB:')
  print(f" - AuctionID: {v.AuctionID}")
  print(f" - SellerName: {v.SellerName}")
  print(f" - ITID: {v.ITID}")
  print(f" - Type: {v.Type}")
  print(f" - count: {v.count}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - NowPrice: {v.NowPrice}")
  print(f" - MaxPrice: {v.MaxPrice}")
  print(f" - BuyerName: {v.BuyerName}")
  print(f" - DeleteTime: {v.DeleteTime}")

def print_ZC_AUCTION_RESULT(v):
  print('Fields of ZC_AUCTION_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_AUCTION_WINDOWS(v):
  print('Fields of ZC_AUCTION_WINDOWS:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_ZC_AUTORUN_SKILL(v):
  print('Fields of ZC_AUTORUN_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - type: {v.type}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - skillName: {v.skillName}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_AUTOSPELLLIST(v):
  print('Fields of ZC_AUTOSPELLLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")

def print_ZC_BABYMSG(v):
  print('Fields of ZC_BABYMSG:')
  print(f" - packetId: {v.packetId}")
  print(f" - MsgNo: {v.MsgNo}")

def print_ZC_BANKING_CHECK(v):
  print('Fields of ZC_BANKING_CHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Money: {v.Money}")
  print(f" - Reason: {v.Reason}")

def print_ZC_BAN_LIST(v):
  print('Fields of ZC_BAN_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - banList: {v.banList}")

def print_ZC_BAN_LIST_SUB(v):
  print('Fields of ZC_BAN_LIST_SUB:')
  print(f" - charname: {v.charname}")
  print(f" - account: {v.account}")
  print(f" - reason: {v.reason}")

def print_ZC_BATTLEFIELD_CHAT(v):
  print('Fields of ZC_BATTLEFIELD_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - accountID: {v.accountID}")
  print(f" - name: {v.name}")
  print(f" - msg: {v.msg}")

def print_ZC_BATTLEFIELD_NOTIFY_CAMPINFO(v):
  print('Fields of ZC_BATTLEFIELD_NOTIFY_CAMPINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - accountID: {v.accountID}")
  print(f" - name: {v.name}")
  print(f" - camp: {v.camp}")

def print_ZC_BATTLEFIELD_NOTIFY_HP(v):
  print('Fields of ZC_BATTLEFIELD_NOTIFY_HP:')
  print(f" - packetId: {v.packetId}")
  print(f" - accountID: {v.accountID}")
  print(f" - name: {v.name}")
  print(f" - hp: {v.hp}")
  print(f" - maxHp: {v.maxHp}")

def print_ZC_BATTLEFIELD_NOTIFY_HP2(v):
  print('Fields of ZC_BATTLEFIELD_NOTIFY_HP2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - hp: {v.hp}")
  print(f" - maxHp: {v.maxHp}")

def print_ZC_BATTLEFIELD_NOTIFY_POINT(v):
  print('Fields of ZC_BATTLEFIELD_NOTIFY_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - pointCampA: {v.pointCampA}")
  print(f" - pointCampB: {v.pointCampB}")

def print_ZC_BATTLEFIELD_NOTIFY_POSITION(v):
  print('Fields of ZC_BATTLEFIELD_NOTIFY_POSITION:')
  print(f" - packetId: {v.packetId}")
  print(f" - accountID: {v.accountID}")
  print(f" - name: {v.name}")
  print(f" - job: {v.job}")
  print(f" - x: {v.x}")
  print(f" - y: {v.y}")

def print_ZC_BATTLE_FIELD_LIST(v):
  print('Fields of ZC_BATTLE_FIELD_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Count: {v.Count}")
  print(f" - ack_type: {v.ack_type}")
  print(f" - BattleFieldList: {v.BattleFieldList}")

def print_ZC_BATTLE_FIELD_LIST_INFO(v):
  print('Fields of ZC_BATTLE_FIELD_LIST_INFO:')
  print(f" - BFNO: {v.BFNO}")
  print(f" - BattleFieldName: {v.BattleFieldName}")
  print(f" - JoinTeam: {v.JoinTeam}")

def print_ZC_BATTLE_JOIN_DISABLE_STATE(v):
  print('Fields of ZC_BATTLE_JOIN_DISABLE_STATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Enable: {v.Enable}")

def print_ZC_BATTLE_JOIN_NOTI_DEFER(v):
  print('Fields of ZC_BATTLE_JOIN_NOTI_DEFER:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")

def print_ZC_BATTLE_NOTI_START_STEP(v):
  print('Fields of ZC_BATTLE_NOTI_START_STEP:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")
  print(f" - Result: {v.Result}")

def print_ZC_BLACKSMITH_POINT(v):
  print('Fields of ZC_BLACKSMITH_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Point: {v.Point}")
  print(f" - TotalPoint: {v.TotalPoint}")

def print_ZC_BLACKSMITH_RANK(v):
  print('Fields of ZC_BLACKSMITH_RANK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Name: {v.Name}")
  print(f" - Point: {v.Point}")

def print_ZC_BLADESTOP(v):
  print('Fields of ZC_BLADESTOP:')
  print(f" - packetId: {v.packetId}")
  print(f" - srcAID: {v.srcAID}")
  print(f" - destAID: {v.destAID}")
  print(f" - flag: {v.flag}")

def print_ZC_BLOCK_CHARACTER_SUB(v):
  print('Fields of ZC_BLOCK_CHARACTER_SUB:')
  print(f" - GID: {v.GID}")
  print(f" - szExpireDate: {v.szExpireDate}")

def print_ZC_BOSS_INFO(v):
  print('Fields of ZC_BOSS_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - infoType: {v.infoType}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - minHour: {v.minHour}")
  print(f" - minMinute: {v.minMinute}")
  print(f" - maxHour: {v.maxHour}")
  print(f" - maxMinute: {v.maxMinute}")
  print(f" - name: {v.name}")

def print_ZC_BROADCAST(v):
  print('Fields of ZC_BROADCAST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_ZC_BROADCAST2(v):
  print('Fields of ZC_BROADCAST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - fontColor: {v.fontColor}")
  print(f" - fontType: {v.fontType}")
  print(f" - fontSize: {v.fontSize}")
  print(f" - fontAlign: {v.fontAlign}")
  print(f" - fontY: {v.fontY}")
  print(f" - msg: {v.msg}")

def print_ZC_BROADCAST4(v):
  print('Fields of ZC_BROADCAST4:')
  print(f" - packetId: {v.packetId}")
  print(f" - PakcetType: {v.PakcetType}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Msgtype: {v.Msgtype}")
  print(f" - ColorRGB: {v.ColorRGB}")
  print(f" - msg: {v.msg}")

def print_ZC_BUYING_STORE_ENTRY(v):
  print('Fields of ZC_BUYING_STORE_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - makerAID: {v.makerAID}")
  print(f" - storeName: {v.storeName}")

def print_ZC_CANCEL_BATTLE_FIELD(v):
  print('Fields of ZC_CANCEL_BATTLE_FIELD:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")
  print(f" - Result: {v.Result}")

def print_ZC_CANCEL_EXCHANGE_ITEM(v):
  print('Fields of ZC_CANCEL_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")

def print_ZC_CARTOFF(v):
  print('Fields of ZC_CARTOFF:')
  print(f" - packetId: {v.packetId}")

def print_ZC_CART_EQUIPMENT_ITEMLIST(v):
  print('Fields of ZC_CART_EQUIPMENT_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_CART_EQUIPMENT_ITEMLIST2(v):
  print('Fields of ZC_CART_EQUIPMENT_ITEMLIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_CART_EQUIPMENT_ITEMLIST2_SUB(v):
  print('Fields of ZC_CART_EQUIPMENT_ITEMLIST2_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_CART_EQUIPMENT_ITEMLIST3(v):
  print('Fields of ZC_CART_EQUIPMENT_ITEMLIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - equipmentList: {v.equipmentList}")

def print_ZC_CART_EQUIPMENT_ITEMLIST3_SUB(v):
  print('Fields of ZC_CART_EQUIPMENT_ITEMLIST3_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")

def print_ZC_CART_EQUIPMENT_ITEMLIST_SUB(v):
  print('Fields of ZC_CART_EQUIPMENT_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_CART_ITEMLIST_EQUIP_V5(v):
  print('Fields of ZC_CART_ITEMLIST_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_CART_ITEMLIST_EQUIP_V5_ITEMINFO(v):
  print('Fields of ZC_CART_ITEMLIST_EQUIP_V5_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - Flag: {v.Flag}")

def print_ZC_CART_ITEMLIST_EQUIP_V6(v):
  print('Fields of ZC_CART_ITEMLIST_EQUIP_V6:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Items: {v.Items}")

def print_ZC_CART_ITEMLIST_EQUIP_V6_ITEMINFO(v):
  print('Fields of ZC_CART_ITEMLIST_EQUIP_V6_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - nRandomOptionCnt: {v.nRandomOptionCnt}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")
  print(f" - Flag: {v.Flag}")

def print_ZC_CART_ITEMLIST_NORMAL_V5(v):
  print('Fields of ZC_CART_ITEMLIST_NORMAL_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_CART_ITEMLIST_NORMAL_V5_ITEMINFO(v):
  print('Fields of ZC_CART_ITEMLIST_NORMAL_V5_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - Flag: {v.Flag}")

def print_ZC_CART_NORMAL_ITEMLIST(v):
  print('Fields of ZC_CART_NORMAL_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_CART_NORMAL_ITEMLIST2(v):
  print('Fields of ZC_CART_NORMAL_ITEMLIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_CART_NORMAL_ITEMLIST2_SUB(v):
  print('Fields of ZC_CART_NORMAL_ITEMLIST2_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_CART_NORMAL_ITEMLIST3(v):
  print('Fields of ZC_CART_NORMAL_ITEMLIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ItemInfo: {v.ItemInfo}")

def print_ZC_CART_NORMAL_ITEMLIST3_ITEMINFO(v):
  print('Fields of ZC_CART_NORMAL_ITEMLIST3_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_CART_NORMAL_ITEMLIST_SUB(v):
  print('Fields of ZC_CART_NORMAL_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")

def print_ZC_CASH_ITEM_DELETE(v):
  print('Fields of ZC_CASH_ITEM_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")

def print_ZC_CASH_TIME_COUNTER(v):
  print('Fields of ZC_CASH_TIME_COUNTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - RemainSecond: {v.RemainSecond}")

def print_ZC_CHANGESTATE_MER(v):
  print('Fields of ZC_CHANGESTATE_MER:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - state: {v.state}")
  print(f" - GID: {v.GID}")
  print(f" - data: {v.data}")

def print_ZC_CHANGESTATE_PET(v):
  print('Fields of ZC_CHANGESTATE_PET:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - GID: {v.GID}")
  print(f" - data: {v.data}")

def print_ZC_CHANGE_CHATROOM(v):
  print('Fields of ZC_CHANGE_CHATROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - roomID: {v.roomID}")
  print(f" - maxcount: {v.maxcount}")
  print(f" - curcount: {v.curcount}")
  print(f" - type: {v.type}")
  print(f" - title: {v.title}")

def print_ZC_CHANGE_DIRECTION(v):
  print('Fields of ZC_CHANGE_DIRECTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - headDir: {v.headDir}")
  print(f" - dir: {v.dir}")

def print_ZC_CHANGE_GROUP_MASTER(v):
  print('Fields of ZC_CHANGE_GROUP_MASTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - OldMasterAID: {v.OldMasterAID}")
  print(f" - NewMasterAID: {v.NewMasterAID}")

def print_ZC_CHANGE_GUILD(v):
  print('Fields of ZC_CHANGE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GDID: {v.GDID}")
  print(f" - emblemVersion: {v.emblemVersion}")

def print_ZC_CHECK_RECEIVE_CHARACTER_NAME(v):
  print('Fields of ZC_CHECK_RECEIVE_CHARACTER_NAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - Job: {v.Job}")
  print(f" - Clevel: {v.Clevel}")

def print_ZC_CLANINFO(v):
  print('Fields of ZC_CLANINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - EmblemNum: {v.EmblemNum}")
  print(f" - ClanName: {v.ClanName}")
  print(f" - Mastername: {v.Mastername}")
  print(f" - ManageMap: {v.ManageMap}")
  print(f" - Num_AllyClan: {v.Num_AllyClan}")
  print(f" - Num_HostileClan: {v.Num_HostileClan}")

def print_ZC_CLEAR_DIALOG(v):
  print('Fields of ZC_CLEAR_DIALOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_ZC_CLOSE_BARGAIN_SALE_TOOL(v):
  print('Fields of ZC_CLOSE_BARGAIN_SALE_TOOL:')
  print(f" - packetId: {v.packetId}")

def print_ZC_CLOSE_DIALOG(v):
  print('Fields of ZC_CLOSE_DIALOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_ZC_CLOSE_STORE(v):
  print('Fields of ZC_CLOSE_STORE:')
  print(f" - packetId: {v.packetId}")

def print_ZC_COMBODELAY(v):
  print('Fields of ZC_COMBODELAY:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - delayTime: {v.delayTime}")

def print_ZC_COMPASS(v):
  print('Fields of ZC_COMPASS:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")
  print(f" - type: {v.type}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - id: {v.id}")
  print(f" - color: {v.color}")

def print_ZC_CONCLUDE_EXCHANGE_ITEM(v):
  print('Fields of ZC_CONCLUDE_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - who: {v.who}")

def print_ZC_CONFIG(v):
  print('Fields of ZC_CONFIG:')
  print(f" - packetId: {v.packetId}")
  print(f" - Config: {v.Config}")
  print(f" - Value: {v.Value}")

def print_ZC_CONFIG_NOTIFY(v):
  print('Fields of ZC_CONFIG_NOTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - bOpenEquipmentWin: {v.bOpenEquipmentWin}")

def print_ZC_CONGRATULATION(v):
  print('Fields of ZC_CONGRATULATION:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_COSTUME_SPRITE_CHANGE(v):
  print('Fields of ZC_COSTUME_SPRITE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - type: {v.type}")
  print(f" - value: {v.value}")

def print_ZC_COUPLENAME(v):
  print('Fields of ZC_COUPLENAME:')
  print(f" - packetId: {v.packetId}")
  print(f" - CoupleName: {v.CoupleName}")

def print_ZC_COUPLESTATUS(v):
  print('Fields of ZC_COUPLESTATUS:')
  print(f" - packetId: {v.packetId}")
  print(f" - statusType: {v.statusType}")
  print(f" - defaultStatus: {v.defaultStatus}")
  print(f" - plusStatus: {v.plusStatus}")

def print_ZC_C_MARKERINFO(v):
  print('Fields of ZC_C_MARKERINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_DEATH_QUESTION(v):
  print('Fields of ZC_DEATH_QUESTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - Qcategory: {v.Qcategory}")
  print(f" - Qnum: {v.Qnum}")

def print_ZC_DEFINE_CHECK(v):
  print('Fields of ZC_DEFINE_CHECK:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Result: {v.Result}")

def print_ZC_DELETEITEM_FROM_MCSTORE(v):
  print('Fields of ZC_DELETEITEM_FROM_MCSTORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_ZC_DELETEITEM_FROM_MCSTORE2(v):
  print('Fields of ZC_DELETEITEM_FROM_MCSTORE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - ToGID: {v.ToGID}")
  print(f" - Date: {v.Date}")
  print(f" - Zeny: {v.Zeny}")

def print_ZC_DELETE_FRIENDS(v):
  print('Fields of ZC_DELETE_FRIENDS:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")

def print_ZC_DELETE_ITEM_FROM_BODY(v):
  print('Fields of ZC_DELETE_ITEM_FROM_BODY:')
  print(f" - packetId: {v.packetId}")
  print(f" - DeleteType: {v.DeleteType}")
  print(f" - Index: {v.Index}")
  print(f" - Count: {v.Count}")

def print_ZC_DELETE_ITEM_FROM_CART(v):
  print('Fields of ZC_DELETE_ITEM_FROM_CART:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_ZC_DELETE_ITEM_FROM_STORE(v):
  print('Fields of ZC_DELETE_ITEM_FROM_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")

def print_ZC_DELETE_MEMBER_FROM_GROUP(v):
  print('Fields of ZC_DELETE_MEMBER_FROM_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - characterName: {v.characterName}")
  print(f" - result: {v.result}")

def print_ZC_DELETE_RELATED_GUILD(v):
  print('Fields of ZC_DELETE_RELATED_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - OpponentGDID: {v.OpponentGDID}")
  print(f" - Relation: {v.Relation}")

def print_ZC_DEL_QUEST(v):
  print('Fields of ZC_DEL_QUEST:')
  print(f" - packetId: {v.packetId}")
  print(f" - questID: {v.questID}")

def print_ZC_DESTROY_ROOM(v):
  print('Fields of ZC_DESTROY_ROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - roomID: {v.roomID}")

def print_ZC_DEVOTIONLIST(v):
  print('Fields of ZC_DEVOTIONLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - myAID: {v.myAID}")
  print(f" - AID: {v.AID}")
  print(f" - range: {v.range}")

def print_ZC_DISAPPEAR_BUYING_STORE_ENTRY(v):
  print('Fields of ZC_DISAPPEAR_BUYING_STORE_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - makerAID: {v.makerAID}")

def print_ZC_DISAPPEAR_ENTRY(v):
  print('Fields of ZC_DISAPPEAR_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - makerAID: {v.makerAID}")

def print_ZC_DISPATCH_TIMING_INFO_CHN(v):
  print('Fields of ZC_DISPATCH_TIMING_INFO_CHN:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Balance: {v.Balance}")
  print(f" - Effective_dTime: {v.Effective_dTime}")
  print(f" - Reason: {v.Reason}")

def print_ZC_DISPEL(v):
  print('Fields of ZC_DISPEL:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_DIVORCE(v):
  print('Fields of ZC_DIVORCE:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")

def print_ZC_DRESSROOM_OPEN(v):
  print('Fields of ZC_DRESSROOM_OPEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - m_ViewType: {v.m_ViewType}")

def print_ZC_DYNAMICNPC_CREATE_RESULT(v):
  print('Fields of ZC_DYNAMICNPC_CREATE_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_EFST_SET_ENTER(v):
  print('Fields of ZC_EFST_SET_ENTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - hEFST: {v.hEFST}")
  print(f" - Time: {v.Time}")
  print(f" - Val1: {v.Val1}")
  print(f" - Val2: {v.Val2}")
  print(f" - Val3: {v.Val3}")

def print_ZC_EFST_SET_ENTER2(v):
  print('Fields of ZC_EFST_SET_ENTER2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - hEFST: {v.hEFST}")
  print(f" - MaxMS: {v.MaxMS}")
  print(f" - Time: {v.Time}")
  print(f" - Val1: {v.Val1}")
  print(f" - Val2: {v.Val2}")
  print(f" - Val3: {v.Val3}")

def print_ZC_EL_INIT(v):
  print('Fields of ZC_EL_INIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - hp: {v.hp}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - sp: {v.sp}")
  print(f" - maxSP: {v.maxSP}")

def print_ZC_EL_PAR_CHANGE(v):
  print('Fields of ZC_EL_PAR_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - var: {v.var}")
  print(f" - value: {v.value}")

def print_ZC_EMOTION(v):
  print('Fields of ZC_EMOTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - type: {v.type}")

def print_ZC_ENTER_ROOM(v):
  print('Fields of ZC_ENTER_ROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - roomID: {v.roomID}")
  print(f" - members: {v.members}")

def print_ZC_ENTER_ROOM_MEMBERS(v):
  print('Fields of ZC_ENTER_ROOM_MEMBERS:')
  print(f" - role: {v.role}")
  print(f" - name: {v.name}")

def print_ZC_ENTRY_QUEUE_INIT(v):
  print('Fields of ZC_ENTRY_QUEUE_INIT:')
  print(f" - packetId: {v.packetId}")

def print_ZC_EQUIPITEM_DAMAGED(v):
  print('Fields of ZC_EQUIPITEM_DAMAGED:')
  print(f" - packetId: {v.packetId}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - accountID: {v.accountID}")

def print_ZC_EQUIPMENT_ITEMLIST(v):
  print('Fields of ZC_EQUIPMENT_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_EQUIPMENT_ITEMLIST2(v):
  print('Fields of ZC_EQUIPMENT_ITEMLIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_EQUIPMENT_ITEMLIST2_SUB(v):
  print('Fields of ZC_EQUIPMENT_ITEMLIST2_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_EQUIPMENT_ITEMLIST3(v):
  print('Fields of ZC_EQUIPMENT_ITEMLIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - equipmentList: {v.equipmentList}")

def print_ZC_EQUIPMENT_ITEMLIST3_SUB(v):
  print('Fields of ZC_EQUIPMENT_ITEMLIST3_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")

def print_ZC_EQUIPMENT_ITEMLIST_SUB(v):
  print('Fields of ZC_EQUIPMENT_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_EQUIPWIN_MICROSCOPE(v):
  print('Fields of ZC_EQUIPWIN_MICROSCOPE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - characterName: {v.characterName}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - sex: {v.sex}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_EQUIPWIN_MICROSCOPE2(v):
  print('Fields of ZC_EQUIPWIN_MICROSCOPE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - characterName: {v.characterName}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - robe: {v.robe}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - sex: {v.sex}")

def print_ZC_EQUIPWIN_MICROSCOPE_ITEMINFO(v):
  print('Fields of ZC_EQUIPWIN_MICROSCOPE_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")

def print_ZC_EQUIPWIN_MICROSCOPE_V5(v):
  print('Fields of ZC_EQUIPWIN_MICROSCOPE_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - Length: {v.Length}")
  print(f" - characterName: {v.characterName}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - robe: {v.robe}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - sex: {v.sex}")

def print_ZC_EQUIP_ARROW(v):
  print('Fields of ZC_EQUIP_ARROW:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_ZC_ES_GOTO(v):
  print('Fields of ZC_ES_GOTO:')
  print(f" - packetId: {v.packetId}")
  print(f" - esNo: {v.esNo}")

def print_ZC_ES_LIST(v):
  print('Fields of ZC_ES_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Count: {v.Count}")

def print_ZC_ES_NOTI_MYINFO(v):
  print('Fields of ZC_ES_NOTI_MYINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - esNo: {v.esNo}")
  print(f" - esname: {v.esname}")

def print_ZC_ES_READY(v):
  print('Fields of ZC_ES_READY:')
  print(f" - packetId: {v.packetId}")
  print(f" - esNo: {v.esNo}")

def print_ZC_ES_RESULT(v):
  print('Fields of ZC_ES_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - esNo: {v.esNo}")
  print(f" - esMsg: {v.esMsg}")

def print_ZC_EXCHANGEITEM_UNDO(v):
  print('Fields of ZC_EXCHANGEITEM_UNDO:')
  print(f" - packetId: {v.packetId}")

def print_ZC_EXEC_EXCHANGE_ITEM(v):
  print('Fields of ZC_EXEC_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_FAILED_GET_ITEM_FROM_ZONEDA(v):
  print('Fields of ZC_FAILED_GET_ITEM_FROM_ZONEDA:')
  print(f" - packetId: {v.packetId}")

def print_ZC_FAILED_OPEN_BUYING_STORE_TO_BUYER(v):
  print('Fields of ZC_FAILED_OPEN_BUYING_STORE_TO_BUYER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - total_weight: {v.total_weight}")

def print_ZC_FAILED_TRADE_BUYING_STORE_TO_BUYER(v):
  print('Fields of ZC_FAILED_TRADE_BUYING_STORE_TO_BUYER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_FAILED_TRADE_BUYING_STORE_TO_SELLER(v):
  print('Fields of ZC_FAILED_TRADE_BUYING_STORE_TO_SELLER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - ITID: {v.ITID}")

def print_ZC_FASTMOVE(v):
  print('Fields of ZC_FASTMOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - targetXpos: {v.targetXpos}")
  print(f" - targetYpos: {v.targetYpos}")

def print_ZC_FATIGUE_CHN(v):
  print('Fields of ZC_FATIGUE_CHN:')
  print(f" - packetId: {v.packetId}")
  print(f" - Level: {v.Level}")
  print(f" - TotalPlayTime: {v.TotalPlayTime}")

def print_ZC_FEED_PET(v):
  print('Fields of ZC_FEED_PET:')
  print(f" - packetId: {v.packetId}")
  print(f" - cRet: {v.cRet}")
  print(f" - ITID: {v.ITID}")

def print_ZC_FORMATSTRING_MSG(v):
  print('Fields of ZC_FORMATSTRING_MSG:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")
  print(f" - value: {v.value}")

def print_ZC_FRIENDS_LIST(v):
  print('Fields of ZC_FRIENDS_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - friendsList: {v.friendsList}")

def print_ZC_FRIENDS_LIST_SUB(v):
  print('Fields of ZC_FRIENDS_LIST_SUB:')
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - Name: {v.Name}")

def print_ZC_FRIENDS_STATE(v):
  print('Fields of ZC_FRIENDS_STATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - State: {v.State}")

def print_ZC_GAMEGUARD_LINGO_KEY(v):
  print('Fields of ZC_GAMEGUARD_LINGO_KEY:')
  print(f" - packetId: {v.packetId}")
  print(f" - packetType: {v.packetType}")
  print(f" - dwAlgNum: {v.dwAlgNum}")
  print(f" - dwAlgKey1: {v.dwAlgKey1}")
  print(f" - dwAlgKey2: {v.dwAlgKey2}")
  print(f" - dwSeed: {v.dwSeed}")

def print_ZC_GAME_GUARD(v):
  print('Fields of ZC_GAME_GUARD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AuthData: {v.AuthData}")

def print_ZC_GANGSI_POINT(v):
  print('Fields of ZC_GANGSI_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Point: {v.Point}")
  print(f" - TotalPoint: {v.TotalPoint}")
  print(f" - PacketSwitch: {v.PacketSwitch}")

def print_ZC_GANGSI_RANK(v):
  print('Fields of ZC_GANGSI_RANK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Name: {v.Name}")
  print(f" - Point: {v.Point}")
  print(f" - PacketSwitch: {v.PacketSwitch}")

def print_ZC_GOLDPCCAFE_POINT(v):
  print('Fields of ZC_GOLDPCCAFE_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - bActive: {v.bActive}")
  print(f" - UnitPoint: {v.UnitPoint}")
  print(f" - Point: {v.Point}")
  print(f" - AccumulatePlaySecond: {v.AccumulatePlaySecond}")

def print_ZC_GPK_DYNCODE(v):
  print('Fields of ZC_GPK_DYNCODE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - code: {v.code}")

def print_ZC_GROUPINFO_CHANGE(v):
  print('Fields of ZC_GROUPINFO_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - expOption: {v.expOption}")

def print_ZC_GROUP_LIST(v):
  print('Fields of ZC_GROUP_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - groupName: {v.groupName}")
  print(f" - groupList: {v.groupList}")

def print_ZC_GROUP_LIST_SUB(v):
  print('Fields of ZC_GROUP_LIST_SUB:')
  print(f" - AID: {v.AID}")
  print(f" - characterName: {v.characterName}")
  print(f" - mapName: {v.mapName}")
  print(f" - role: {v.role}")
  print(f" - state: {v.state}")

def print_ZC_GUILDSTORAGE_ITEMLIST_EQUIP_V5(v):
  print('Fields of ZC_GUILDSTORAGE_ITEMLIST_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - StoreName: {v.StoreName}")

def print_ZC_GUILDSTORAGE_ITEMLIST_EQUIP_V6(v):
  print('Fields of ZC_GUILDSTORAGE_ITEMLIST_EQUIP_V6:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - StoreName: {v.StoreName}")

def print_ZC_GUILDSTORAGE_ITEMLIST_NORMAL_V5(v):
  print('Fields of ZC_GUILDSTORAGE_ITEMLIST_NORMAL_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - StoreName: {v.StoreName}")

def print_ZC_GUILD_CHAT(v):
  print('Fields of ZC_GUILD_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_ZC_GUILD_EMBLEM_IMG(v):
  print('Fields of ZC_GUILD_EMBLEM_IMG:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - GDID: {v.GDID}")
  print(f" - emblemVersion: {v.emblemVersion}")
  print(f" - img: {v.img}")

def print_ZC_GUILD_INFO(v):
  print('Fields of ZC_GUILD_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - level: {v.level}")
  print(f" - userNum: {v.userNum}")
  print(f" - maxUserNum: {v.maxUserNum}")
  print(f" - userAverageLevel: {v.userAverageLevel}")
  print(f" - exp: {v.exp}")
  print(f" - maxExp: {v.maxExp}")
  print(f" - point: {v.point}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - emblemVersion: {v.emblemVersion}")
  print(f" - guildname: {v.guildname}")
  print(f" - masterName: {v.masterName}")
  print(f" - manageLand: {v.manageLand}")

def print_ZC_GUILD_INFO2(v):
  print('Fields of ZC_GUILD_INFO2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - level: {v.level}")
  print(f" - userNum: {v.userNum}")
  print(f" - maxUserNum: {v.maxUserNum}")
  print(f" - userAverageLevel: {v.userAverageLevel}")
  print(f" - exp: {v.exp}")
  print(f" - maxExp: {v.maxExp}")
  print(f" - point: {v.point}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - emblemVersion: {v.emblemVersion}")
  print(f" - guildname: {v.guildname}")
  print(f" - masterName: {v.masterName}")
  print(f" - manageLand: {v.manageLand}")
  print(f" - zeny: {v.zeny}")

def print_ZC_GUILD_MEMBER_MAP_CHANGE(v):
  print('Fields of ZC_GUILD_MEMBER_MAP_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - AID: {v.AID}")
  print(f" - mapName: {v.mapName}")

def print_ZC_GUILD_NOTICE(v):
  print('Fields of ZC_GUILD_NOTICE:')
  print(f" - packetId: {v.packetId}")
  print(f" - subject: {v.subject}")
  print(f" - notice: {v.notice}")

def print_ZC_GUILD_SKILLINFO(v):
  print('Fields of ZC_GUILD_SKILLINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - skillPoint: {v.skillPoint}")
  print(f" - skillInfo: {v.skillInfo}")

def print_ZC_GUILD_SKILLINFO_SUB(v):
  print('Fields of ZC_GUILD_SKILLINFO_SUB:')
  print(f" - SKID: {v.SKID}")
  print(f" - type: {v.type}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - skillName: {v.skillName}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_GUILD_ZENY_ACK(v):
  print('Fields of ZC_GUILD_ZENY_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - ret: {v.ret}")

def print_ZC_HACKSH_ERROR_MSG(v):
  print('Fields of ZC_HACKSH_ERROR_MSG:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorID: {v.ErrorID}")

def print_ZC_HIGHJUMP(v):
  print('Fields of ZC_HIGHJUMP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_HO_PAR_CHANGE(v):
  print('Fields of ZC_HO_PAR_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - var: {v.var}")
  print(f" - value: {v.value}")

def print_ZC_HP_INFO(v):
  print('Fields of ZC_HP_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - HP: {v.HP}")
  print(f" - MaxHP: {v.MaxHP}")

def print_ZC_HUNTINGLIST(v):
  print('Fields of ZC_HUNTINGLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - huntingList: {v.huntingList}")

def print_ZC_HUNTINGLIST_SUB(v):
  print('Fields of ZC_HUNTINGLIST_SUB:')
  print(f" - questID: {v.questID}")
  print(f" - mobGID: {v.mobGID}")
  print(f" - maxCount: {v.maxCount}")
  print(f" - count: {v.count}")

def print_ZC_INFO_REMAINTIME(v):
  print('Fields of ZC_INFO_REMAINTIME:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")
  print(f" - RemainTime: {v.RemainTime}")

def print_ZC_INVENTORY_ITEMLIST_EQUIP(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_EQUIP:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_INVENTORY_ITEMLIST_EQUIP_SUB(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_EQUIP_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - Flag: {v.Flag}")

def print_ZC_INVENTORY_ITEMLIST_EQUIP_V5(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Items: {v.Items}")

def print_ZC_INVENTORY_ITEMLIST_EQUIP_V5_ITEMINFO(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_EQUIP_V5_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - Flag: {v.Flag}")

def print_ZC_INVENTORY_ITEMLIST_EQUIP_V6(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_EQUIP_V6:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Items: {v.Items}")

def print_ZC_INVENTORY_ITEMLIST_EQUIP_V6_ITEMINFO(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_EQUIP_V6_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - nRandomOptionCnt: {v.nRandomOptionCnt}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")
  print(f" - Flag: {v.Flag}")

def print_ZC_INVENTORY_ITEMLIST_NORMAL(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_NORMAL:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_INVENTORY_ITEMLIST_NORMAL_SUB(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_NORMAL_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - Flag: {v.Flag}")

def print_ZC_INVENTORY_ITEMLIST_NORMAL_V5(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_NORMAL_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Items: {v.Items}")

def print_ZC_INVENTORY_ITEMLIST_NORMAL_v5_ITEMINFO(v):
  print('Fields of ZC_INVENTORY_ITEMLIST_NORMAL_v5_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - Flag: {v.Flag}")

def print_ZC_INVENTORY_TAB(v):
  print('Fields of ZC_INVENTORY_TAB:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - NORMALorPRIVATE: {v.NORMALorPRIVATE}")

def print_ZC_IRMAIL_NOTIFY(v):
  print('Fields of ZC_IRMAIL_NOTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - office: {v.office}")
  print(f" - id: {v.id}")

def print_ZC_IRMAIL_SEND_RES(v):
  print('Fields of ZC_IRMAIL_SEND_RES:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_ISVR_DISCONNECT(v):
  print('Fields of ZC_ISVR_DISCONNECT:')
  print(f" - packetId: {v.packetId}")

def print_ZC_ITEMCOMPOSITION_LIST(v):
  print('Fields of ZC_ITEMCOMPOSITION_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ITIDList: {v.ITIDList}")

def print_ZC_ITEMIDENTIFY_LIST(v):
  print('Fields of ZC_ITEMIDENTIFY_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ITIDList: {v.ITIDList}")

def print_ZC_ITEMLISTWIN_OPEN(v):
  print('Fields of ZC_ITEMLISTWIN_OPEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_ZC_ITEM_DELETE_BUYING_STORE(v):
  print('Fields of ZC_ITEM_DELETE_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - zeny: {v.zeny}")

def print_ZC_ITEM_DISAPPEAR(v):
  print('Fields of ZC_ITEM_DISAPPEAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")

def print_ZC_ITEM_ENTRY(v):
  print('Fields of ZC_ITEM_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - count: {v.count}")
  print(f" - subX: {v.subX}")
  print(f" - subY: {v.subY}")

def print_ZC_ITEM_FALL_ENTRY(v):
  print('Fields of ZC_ITEM_FALL_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - subX: {v.subX}")
  print(f" - subY: {v.subY}")
  print(f" - count: {v.count}")

def print_ZC_ITEM_FALL_ENTRY4(v):
  print('Fields of ZC_ITEM_FALL_ENTRY4:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - subX: {v.subX}")
  print(f" - subY: {v.subY}")
  print(f" - count: {v.count}")

def print_ZC_ITEM_PICKUP_ACK(v):
  print('Fields of ZC_ITEM_PICKUP_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - location: {v.location}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")

def print_ZC_ITEM_PICKUP_ACK2(v):
  print('Fields of ZC_ITEM_PICKUP_ACK2:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - location: {v.location}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_ITEM_PICKUP_ACK3(v):
  print('Fields of ZC_ITEM_PICKUP_ACK3:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - location: {v.location}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")

def print_ZC_ITEM_PICKUP_ACK_V5(v):
  print('Fields of ZC_ITEM_PICKUP_ACK_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - location: {v.location}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")

def print_ZC_ITEM_PICKUP_ACK_V6(v):
  print('Fields of ZC_ITEM_PICKUP_ACK_V6:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - location: {v.location}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - OptIndex: {v.OptIndex}")
  print(f" - Value: {v.Value}")
  print(f" - Parm1: {v.Parm1}")

def print_ZC_ITEM_PICKUP_PARTY(v):
  print('Fields of ZC_ITEM_PICKUP_PARTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - accountID: {v.accountID}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - location: {v.location}")
  print(f" - type: {v.type}")

def print_ZC_ITEM_THROW_ACK(v):
  print('Fields of ZC_ITEM_THROW_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - count: {v.count}")

def print_ZC_JOIN_BATTLE_FIELD(v):
  print('Fields of ZC_JOIN_BATTLE_FIELD:')
  print(f" - packetId: {v.packetId}")
  print(f" - BFNO: {v.BFNO}")
  print(f" - JoinTeam: {v.JoinTeam}")
  print(f" - Result: {v.Result}")

def print_ZC_LESSEFFECT(v):
  print('Fields of ZC_LESSEFFECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - isLess: {v.isLess}")

def print_ZC_LONGPAR_CHANGE(v):
  print('Fields of ZC_LONGPAR_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - varID: {v.varID}")
  print(f" - amount: {v.amount}")

def print_ZC_MACRO_ITEMPICKUP_FAIL(v):
  print('Fields of ZC_MACRO_ITEMPICKUP_FAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITAID: {v.ITAID}")

def print_ZC_MAIL_RECEIVE(v):
  print('Fields of ZC_MAIL_RECEIVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - MailID: {v.MailID}")
  print(f" - Header: {v.Header}")
  print(f" - FromName: {v.FromName}")

def print_ZC_MAIL_REQ_GET_ITEM(v):
  print('Fields of ZC_MAIL_REQ_GET_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_MAIL_REQ_GET_LIST(v):
  print('Fields of ZC_MAIL_REQ_GET_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - MailNumber: {v.MailNumber}")
  print(f" - mailList: {v.mailList}")

def print_ZC_MAIL_REQ_GET_LIST_SUB(v):
  print('Fields of ZC_MAIL_REQ_GET_LIST_SUB:')
  print(f" - MailID: {v.MailID}")
  print(f" - HEADER: {v.HEADER}")
  print(f" - isOpen: {v.isOpen}")
  print(f" - FromName: {v.FromName}")
  print(f" - DeleteTime: {v.DeleteTime}")

def print_ZC_MAIL_REQ_OPEN(v):
  print('Fields of ZC_MAIL_REQ_OPEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - MailID: {v.MailID}")
  print(f" - Header: {v.Header}")
  print(f" - FromName: {v.FromName}")
  print(f" - DeleteTime: {v.DeleteTime}")
  print(f" - Money: {v.Money}")
  print(f" - count: {v.count}")
  print(f" - ITID: {v.ITID}")
  print(f" - Type: {v.Type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - msg_len: {v.msg_len}")
  print(f" - msg: {v.msg}")

def print_ZC_MAIL_REQ_SEND(v):
  print('Fields of ZC_MAIL_REQ_SEND:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_MAIL_WINDOWS(v):
  print('Fields of ZC_MAIL_WINDOWS:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")

def print_ZC_MAKABLEITEMLIST(v):
  print('Fields of ZC_MAKABLEITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ITID: {v.ITID}")
  print(f" - material_ID: {v.material_ID}")

def print_ZC_MAKINGARROW_LIST(v):
  print('Fields of ZC_MAKINGARROW_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - list: {v.list}")

def print_ZC_MAKINGARROW_LIST_SUB(v):
  print('Fields of ZC_MAKINGARROW_LIST_SUB:')
  print(f" - index: {v.index}")

def print_ZC_MAKINGITEM_LIST(v):
  print('Fields of ZC_MAKINGITEM_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - idList: {v.idList}")

def print_ZC_MAPPROPERTY(v):
  print('Fields of ZC_MAPPROPERTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - type: {v.type}")
  print(f" - mapInfoTable: {v.mapInfoTable}")

def print_ZC_MAPPROPERTY_R2(v):
  print('Fields of ZC_MAPPROPERTY_R2:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - NotifyPropertyBits: {v.NotifyPropertyBits}")

def print_ZC_MEMBERMGR_INFO(v):
  print('Fields of ZC_MEMBERMGR_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - memberInfo: {v.memberInfo}")

def print_ZC_MEMBER_ADD(v):
  print('Fields of ZC_MEMBER_ADD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - head: {v.head}")
  print(f" - headPalette: {v.headPalette}")
  print(f" - sex: {v.sex}")
  print(f" - job: {v.job}")
  print(f" - level: {v.level}")
  print(f" - contributionExp: {v.contributionExp}")
  print(f" - currentState: {v.currentState}")
  print(f" - positionID: {v.positionID}")
  print(f" - intro: {v.intro}")
  print(f" - charname: {v.charname}")

def print_ZC_MEMBER_EXIT(v):
  print('Fields of ZC_MEMBER_EXIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - curcount: {v.curcount}")
  print(f" - name: {v.name}")
  print(f" - type: {v.type}")

def print_ZC_MEMBER_INFO_SUB(v):
  print('Fields of ZC_MEMBER_INFO_SUB:')
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - HeadType: {v.HeadType}")
  print(f" - HeadPalette: {v.HeadPalette}")
  print(f" - Sex: {v.Sex}")
  print(f" - Job: {v.Job}")
  print(f" - Level: {v.Level}")
  print(f" - MemberExp: {v.MemberExp}")
  print(f" - CurrentState: {v.CurrentState}")
  print(f" - GPositionID: {v.GPositionID}")
  print(f" - Memo: {v.Memo}")
  print(f" - CharName: {v.CharName}")

def print_ZC_MEMBER_NEWENTRY(v):
  print('Fields of ZC_MEMBER_NEWENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - curcount: {v.curcount}")
  print(f" - name: {v.name}")

def print_ZC_MEMORIALDUNGEON_INFO(v):
  print('Fields of ZC_MEMORIALDUNGEON_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - MemorialDungeonName: {v.MemorialDungeonName}")
  print(f" - DestroyDate: {v.DestroyDate}")
  print(f" - EnterTimeOutDate: {v.EnterTimeOutDate}")

def print_ZC_MEMORIALDUNGEON_NOTIFY(v):
  print('Fields of ZC_MEMORIALDUNGEON_NOTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")
  print(f" - EnterLimitDate: {v.EnterLimitDate}")

def print_ZC_MEMORIALDUNGEON_SUBSCRIPTION_INFO(v):
  print('Fields of ZC_MEMORIALDUNGEON_SUBSCRIPTION_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - MemorialDungeonName: {v.MemorialDungeonName}")
  print(f" - PriorityOrderNum: {v.PriorityOrderNum}")

def print_ZC_MEMORIALDUNGEON_SUBSCRIPTION_NOTIFY(v):
  print('Fields of ZC_MEMORIALDUNGEON_SUBSCRIPTION_NOTIFY:')
  print(f" - packetId: {v.packetId}")
  print(f" - PriorityOrderNum: {v.PriorityOrderNum}")

def print_ZC_MENU_LIST(v):
  print('Fields of ZC_MENU_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - NAID: {v.NAID}")
  print(f" - msg: {v.msg}")

def print_ZC_MER_INIT(v):
  print('Fields of ZC_MER_INIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - atk: {v.atk}")
  print(f" - Matk: {v.Matk}")
  print(f" - hit: {v.hit}")
  print(f" - critical: {v.critical}")
  print(f" - def: {v._def}")
  print(f" - Mdef: {v.Mdef}")
  print(f" - flee: {v.flee}")
  print(f" - aspd: {v.aspd}")
  print(f" - name: {v.name}")
  print(f" - level: {v.level}")
  print(f" - hp: {v.hp}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - sp: {v.sp}")
  print(f" - maxSP: {v.maxSP}")
  print(f" - ExpireDate: {v.ExpireDate}")
  print(f" - faith: {v.faith}")
  print(f" - toal_call_num: {v.toal_call_num}")
  print(f" - approval_monster_kill_counter: {v.approval_monster_kill_counter}")
  print(f" - ATKRange: {v.ATKRange}")

def print_ZC_MER_PAR_CHANGE(v):
  print('Fields of ZC_MER_PAR_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - var: {v.var}")
  print(f" - value: {v.value}")

def print_ZC_MER_PROPERTY(v):
  print('Fields of ZC_MER_PROPERTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - atk: {v.atk}")
  print(f" - Matk: {v.Matk}")
  print(f" - hit: {v.hit}")
  print(f" - critical: {v.critical}")
  print(f" - def: {v._def}")
  print(f" - Mdef: {v.Mdef}")
  print(f" - flee: {v.flee}")
  print(f" - aspd: {v.aspd}")
  print(f" - name: {v.name}")
  print(f" - level: {v.level}")
  print(f" - hp: {v.hp}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - sp: {v.sp}")
  print(f" - maxSP: {v.maxSP}")
  print(f" - ExpireDate: {v.ExpireDate}")
  print(f" - faith: {v.faith}")
  print(f" - toal_call_num: {v.toal_call_num}")
  print(f" - approval_monster_kill_counter: {v.approval_monster_kill_counter}")

def print_ZC_MER_SKILLINFO_LIST(v):
  print('Fields of ZC_MER_SKILLINFO_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - skillinfoList: {v.skillinfoList}")

def print_ZC_MER_SKILLINFO_LIST_SUB(v):
  print('Fields of ZC_MER_SKILLINFO_LIST_SUB:')
  print(f" - SKID: {v.SKID}")
  print(f" - type: {v.type}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - skillName: {v.skillName}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_MER_SKILLINFO_UPDATE(v):
  print('Fields of ZC_MER_SKILLINFO_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_MILLENNIUMSHIELD(v):
  print('Fields of ZC_MILLENNIUMSHIELD:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - num: {v.num}")
  print(f" - state: {v.state}")

def print_ZC_MONSTER_INFO(v):
  print('Fields of ZC_MONSTER_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - job: {v.job}")
  print(f" - level: {v.level}")
  print(f" - size: {v.size}")
  print(f" - hp: {v.hp}")
  print(f" - def: {v._def}")
  print(f" - raceType: {v.raceType}")
  print(f" - mdefPower: {v.mdefPower}")
  print(f" - property: {v.property}")
  print(f" - water: {v.water}")
  print(f" - earth: {v.earth}")
  print(f" - fire: {v.fire}")
  print(f" - wind: {v.wind}")
  print(f" - poison: {v.poison}")
  print(f" - saint: {v.saint}")
  print(f" - dark: {v.dark}")
  print(f" - mental: {v.mental}")
  print(f" - undead: {v.undead}")

def print_ZC_MONSTER_TALK(v):
  print('Fields of ZC_MONSTER_TALK:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - stateId: {v.stateId}")
  print(f" - skillId: {v.skillId}")
  print(f" - arg1: {v.arg1}")

def print_ZC_MSG(v):
  print('Fields of ZC_MSG:')
  print(f" - packetId: {v.packetId}")
  print(f" - msg: {v.msg}")

def print_ZC_MSG_COLOR(v):
  print('Fields of ZC_MSG_COLOR:')
  print(f" - packetId: {v.packetId}")
  print(f" - msg: {v.msg}")
  print(f" - color: {v.color}")

def print_ZC_MSG_SKILL(v):
  print('Fields of ZC_MSG_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - MSGID: {v.MSGID}")

def print_ZC_MSG_STATE_CHANGE(v):
  print('Fields of ZC_MSG_STATE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - AID: {v.AID}")
  print(f" - state: {v.state}")

def print_ZC_MSG_STATE_CHANGE2(v):
  print('Fields of ZC_MSG_STATE_CHANGE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - AID: {v.AID}")
  print(f" - state: {v.state}")
  print(f" - RemainMS: {v.RemainMS}")
  print(f" - val: {v.val}")

def print_ZC_MSG_STATE_CHANGE3(v):
  print('Fields of ZC_MSG_STATE_CHANGE3:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - AID: {v.AID}")
  print(f" - state: {v.state}")
  print(f" - MaxMS: {v.MaxMS}")
  print(f" - RemainMS: {v.RemainMS}")
  print(f" - val: {v.val}")

def print_ZC_MSG_VALUE(v):
  print('Fields of ZC_MSG_VALUE:')
  print(f" - packetId: {v.packetId}")
  print(f" - msg: {v.msg}")
  print(f" - value: {v.value}")

def print_ZC_MVP(v):
  print('Fields of ZC_MVP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_MVP_GETTING_ITEM(v):
  print('Fields of ZC_MVP_GETTING_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")

def print_ZC_MVP_GETTING_SPECIAL_EXP(v):
  print('Fields of ZC_MVP_GETTING_SPECIAL_EXP:')
  print(f" - packetId: {v.packetId}")
  print(f" - exp: {v.exp}")

def print_ZC_MYGUILD_BASIC_INFO(v):
  print('Fields of ZC_MYGUILD_BASIC_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - info: {v.info}")

def print_ZC_MYGUILD_BASIC_INFO_SUB(v):
  print('Fields of ZC_MYGUILD_BASIC_INFO_SUB:')
  print(f" - GDID: {v.GDID}")
  print(f" - relation: {v.relation}")
  print(f" - GuildName: {v.GuildName}")

def print_ZC_MYITEMLIST_BUYING_STORE(v):
  print('Fields of ZC_MYITEMLIST_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - limitZeny: {v.limitZeny}")
  print(f" - itemList: {v.itemList}")

def print_ZC_MYITEMLIST_BUYING_STORE_ITEMLIST(v):
  print('Fields of ZC_MYITEMLIST_BUYING_STORE_ITEMLIST:')
  print(f" - price: {v.price}")
  print(f" - count: {v.count}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")

def print_ZC_NAVIGATION_ACTIVE(v):
  print('Fields of ZC_NAVIGATION_ACTIVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Type: {v.Type}")
  print(f" - SetType: {v.SetType}")
  print(f" - Hide: {v.Hide}")
  print(f" - MapName: {v.MapName}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - sprIndex: {v.sprIndex}")

def print_ZC_NORMAL_ITEMLIST(v):
  print('Fields of ZC_NORMAL_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_NORMAL_ITEMLIST2(v):
  print('Fields of ZC_NORMAL_ITEMLIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_NORMAL_ITEMLIST2_SUB(v):
  print('Fields of ZC_NORMAL_ITEMLIST2_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_NORMAL_ITEMLIST3(v):
  print('Fields of ZC_NORMAL_ITEMLIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ItemInfo: {v.ItemInfo}")

def print_ZC_NORMAL_ITEMLIST3_ITEMINFO(v):
  print('Fields of ZC_NORMAL_ITEMLIST3_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_NORMAL_ITEMLIST_SUB(v):
  print('Fields of ZC_NORMAL_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")

def print_ZC_NOTIFY_ACT(v):
  print('Fields of ZC_NOTIFY_ACT:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - startTime: {v.startTime}")
  print(f" - attackMT: {v.attackMT}")
  print(f" - attackedMT: {v.attackedMT}")
  print(f" - damage: {v.damage}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")
  print(f" - leftDamage: {v.leftDamage}")

def print_ZC_NOTIFY_ACT2(v):
  print('Fields of ZC_NOTIFY_ACT2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - startTime: {v.startTime}")
  print(f" - attackMT: {v.attackMT}")
  print(f" - attackedMT: {v.attackedMT}")
  print(f" - damage: {v.damage}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")
  print(f" - leftDamage: {v.leftDamage}")

def print_ZC_NOTIFY_ACT3(v):
  print('Fields of ZC_NOTIFY_ACT3:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - startTime: {v.startTime}")
  print(f" - attackMT: {v.attackMT}")
  print(f" - attackedMT: {v.attackedMT}")
  print(f" - damage: {v.damage}")
  print(f" - IsSPDamage: {v.IsSPDamage}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")
  print(f" - leftDamage: {v.leftDamage}")

def print_ZC_NOTIFY_ACTENTRY(v):
  print('Fields of ZC_NOTIFY_ACTENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - action: {v.action}")
  print(f" - actStartTime: {v.actStartTime}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_ACT_POSITION(v):
  print('Fields of ZC_NOTIFY_ACT_POSITION:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - targetGID: {v.targetGID}")
  print(f" - startTime: {v.startTime}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - damage: {v.damage}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")

def print_ZC_NOTIFY_BARGAIN_SALE_CLOSE(v):
  print('Fields of ZC_NOTIFY_BARGAIN_SALE_CLOSE:')
  print(f" - packetId: {v.packetId}")
  print(f" - ItemID: {v.ItemID}")
  print(f" - TabCode: {v.TabCode}")

def print_ZC_NOTIFY_BARGAIN_SALE_SELLING(v):
  print('Fields of ZC_NOTIFY_BARGAIN_SALE_SELLING:')
  print(f" - packetId: {v.packetId}")
  print(f" - ItemID: {v.ItemID}")
  print(f" - TabCode: {v.TabCode}")

def print_ZC_NOTIFY_BIND_ON_EQUIP(v):
  print('Fields of ZC_NOTIFY_BIND_ON_EQUIP:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_ZC_NOTIFY_CARTITEM_COUNTINFO(v):
  print('Fields of ZC_NOTIFY_CARTITEM_COUNTINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - curCount: {v.curCount}")
  print(f" - maxCount: {v.maxCount}")
  print(f" - curWeight: {v.curWeight}")
  print(f" - maxWeight: {v.maxWeight}")

def print_ZC_NOTIFY_CHAT(v):
  print('Fields of ZC_NOTIFY_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - GID: {v.GID}")
  print(f" - msg: {v.msg}")

def print_ZC_NOTIFY_CHAT_PARTY(v):
  print('Fields of ZC_NOTIFY_CHAT_PARTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - msg: {v.msg}")

def print_ZC_NOTIFY_CLAN_CHAT(v):
  print('Fields of ZC_NOTIFY_CLAN_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - charName: {v.charName}")
  print(f" - chat: {v.chat}")

def print_ZC_NOTIFY_CLAN_CONNECTINFO(v):
  print('Fields of ZC_NOTIFY_CLAN_CONNECTINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - NumConnect: {v.NumConnect}")
  print(f" - NumTotal: {v.NumTotal}")

def print_ZC_NOTIFY_CRAZYKILLER(v):
  print('Fields of ZC_NOTIFY_CRAZYKILLER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - isCrazyKiller: {v.isCrazyKiller}")

def print_ZC_NOTIFY_EFFECT(v):
  print('Fields of ZC_NOTIFY_EFFECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - effectID: {v.effectID}")

def print_ZC_NOTIFY_EFFECT2(v):
  print('Fields of ZC_NOTIFY_EFFECT2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - effectID: {v.effectID}")

def print_ZC_NOTIFY_EFFECT3(v):
  print('Fields of ZC_NOTIFY_EFFECT3:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - effectID: {v.effectID}")
  print(f" - numdata: {v.numdata}")

def print_ZC_NOTIFY_ENTRY_QUEUE_ADMISSION(v):
  print('Fields of ZC_NOTIFY_ENTRY_QUEUE_ADMISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_ZC_NOTIFY_ENTRY_QUEUE_APPLY(v):
  print('Fields of ZC_NOTIFY_ENTRY_QUEUE_APPLY:')
  print(f" - packetId: {v.packetId}")
  print(f" - EntryQueueName: {v.EntryQueueName}")
  print(f" - Ranking: {v.Ranking}")

def print_ZC_NOTIFY_EXP(v):
  print('Fields of ZC_NOTIFY_EXP:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - amount: {v.amount}")
  print(f" - varID: {v.varID}")
  print(f" - expType: {v.expType}")

def print_ZC_NOTIFY_FONT(v):
  print('Fields of ZC_NOTIFY_FONT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_GROUNDSKILL(v):
  print('Fields of ZC_NOTIFY_GROUNDSKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - AID: {v.AID}")
  print(f" - level: {v.level}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - startTime: {v.startTime}")

def print_ZC_NOTIFY_HP_TO_GROUPM(v):
  print('Fields of ZC_NOTIFY_HP_TO_GROUPM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")

def print_ZC_NOTIFY_HP_TO_GROUPM_R2(v):
  print('Fields of ZC_NOTIFY_HP_TO_GROUPM_R2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - hp: {v.hp}")
  print(f" - maxhp: {v.maxhp}")

def print_ZC_NOTIFY_INITCHAR(v):
  print('Fields of ZC_NOTIFY_INITCHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - GID: {v.GID}")
  print(f" - Style: {v.Style}")
  print(f" - Item: {v.Item}")

def print_ZC_NOTIFY_LOBBY_ADMISSION(v):
  print('Fields of ZC_NOTIFY_LOBBY_ADMISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - EntryQueueName: {v.EntryQueueName}")
  print(f" - LobbyName: {v.LobbyName}")

def print_ZC_NOTIFY_MANNER_POINT_GIVEN(v):
  print('Fields of ZC_NOTIFY_MANNER_POINT_GIVEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - otherCharName: {v.otherCharName}")

def print_ZC_NOTIFY_MAPINFO(v):
  print('Fields of ZC_NOTIFY_MAPINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_ZC_NOTIFY_MAPPROPERTY(v):
  print('Fields of ZC_NOTIFY_MAPPROPERTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_ZC_NOTIFY_MAPPROPERTY2(v):
  print('Fields of ZC_NOTIFY_MAPPROPERTY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_ZC_NOTIFY_MOVE(v):
  print('Fields of ZC_NOTIFY_MOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - moveStartTime: {v.moveStartTime}")

def print_ZC_NOTIFY_MOVEENTRY(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_MOVEENTRY10(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY10:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")

def print_ZC_NOTIFY_MOVEENTRY11(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY11:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")
  print(f" - body: {v.body}")

def print_ZC_NOTIFY_MOVEENTRY2(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_MOVEENTRY3(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY3:')
  print(f" - packetId: {v.packetId}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_MOVEENTRY4(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY4:')
  print(f" - packetId: {v.packetId}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_MOVEENTRY7(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY7:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - name: {v.name}")

def print_ZC_NOTIFY_MOVEENTRY8(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY8:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_MOVEENTRY9(v):
  print('Fields of ZC_NOTIFY_MOVEENTRY9:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - MoveData: {v.MoveData}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")

def print_ZC_NOTIFY_NEWENTRY(v):
  print('Fields of ZC_NOTIFY_NEWENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_NEWENTRY10(v):
  print('Fields of ZC_NOTIFY_NEWENTRY10:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")

def print_ZC_NOTIFY_NEWENTRY11(v):
  print('Fields of ZC_NOTIFY_NEWENTRY11:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")
  print(f" - body: {v.body}")

def print_ZC_NOTIFY_NEWENTRY2(v):
  print('Fields of ZC_NOTIFY_NEWENTRY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_NEWENTRY3(v):
  print('Fields of ZC_NOTIFY_NEWENTRY3:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_NEWENTRY4(v):
  print('Fields of ZC_NOTIFY_NEWENTRY4:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_NEWENTRY5(v):
  print('Fields of ZC_NOTIFY_NEWENTRY5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - name: {v.name}")

def print_ZC_NOTIFY_NEWENTRY6(v):
  print('Fields of ZC_NOTIFY_NEWENTRY6:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_NEWENTRY7(v):
  print('Fields of ZC_NOTIFY_NEWENTRY7:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")

def print_ZC_NOTIFY_PCBANG(v):
  print('Fields of ZC_NOTIFY_PCBANG:')
  print(f" - packetId: {v.packetId}")

def print_ZC_NOTIFY_PCBANG_PLAYING_TIME(v):
  print('Fields of ZC_NOTIFY_PCBANG_PLAYING_TIME:')
  print(f" - packetId: {v.packetId}")
  print(f" - TimeMinute: {v.TimeMinute}")

def print_ZC_NOTIFY_PKINFO(v):
  print('Fields of ZC_NOTIFY_PKINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - winPoint: {v.winPoint}")
  print(f" - losePoint: {v.losePoint}")
  print(f" - killName: {v.killName}")
  print(f" - killedName: {v.killedName}")
  print(f" - dwLowDateTime: {v.dwLowDateTime}")
  print(f" - dwHighDateTime: {v.dwHighDateTime}")

def print_ZC_NOTIFY_PLAYERCHAT(v):
  print('Fields of ZC_NOTIFY_PLAYERCHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - msg: {v.msg}")

def print_ZC_NOTIFY_PLAYERMOVE(v):
  print('Fields of ZC_NOTIFY_PLAYERMOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - moveStartTime: {v.moveStartTime}")
  print(f" - MoveData: {v.MoveData}")

def print_ZC_NOTIFY_POSITION_TO_GROUPM(v):
  print('Fields of ZC_NOTIFY_POSITION_TO_GROUPM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_NOTIFY_POSITION_TO_GUILDM(v):
  print('Fields of ZC_NOTIFY_POSITION_TO_GUILDM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_NOTIFY_RANKING(v):
  print('Fields of ZC_NOTIFY_RANKING:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - ranking: {v.ranking}")
  print(f" - total: {v.total}")

def print_ZC_NOTIFY_SKILL(v):
  print('Fields of ZC_NOTIFY_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - AID: {v.AID}")
  print(f" - targetID: {v.targetID}")
  print(f" - startTime: {v.startTime}")
  print(f" - attackMT: {v.attackMT}")
  print(f" - attackedMT: {v.attackedMT}")
  print(f" - damage: {v.damage}")
  print(f" - level: {v.level}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")

def print_ZC_NOTIFY_SKILL2(v):
  print('Fields of ZC_NOTIFY_SKILL2:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - AID: {v.AID}")
  print(f" - targetID: {v.targetID}")
  print(f" - startTime: {v.startTime}")
  print(f" - attackMT: {v.attackMT}")
  print(f" - attackedMT: {v.attackedMT}")
  print(f" - damage: {v.damage}")
  print(f" - level: {v.level}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")

def print_ZC_NOTIFY_SKILL_POSITION(v):
  print('Fields of ZC_NOTIFY_SKILL_POSITION:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - AID: {v.AID}")
  print(f" - targetID: {v.targetID}")
  print(f" - startTime: {v.startTime}")
  print(f" - attackMT: {v.attackMT}")
  print(f" - attackedMT: {v.attackedMT}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - damage: {v.damage}")
  print(f" - level: {v.level}")
  print(f" - count: {v.count}")
  print(f" - action: {v.action}")

def print_ZC_NOTIFY_STANDENTRY(v):
  print('Fields of ZC_NOTIFY_STANDENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_STANDENTRY10(v):
  print('Fields of ZC_NOTIFY_STANDENTRY10:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")

def print_ZC_NOTIFY_STANDENTRY11(v):
  print('Fields of ZC_NOTIFY_STANDENTRY11:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")
  print(f" - body: {v.body}")

def print_ZC_NOTIFY_STANDENTRY2(v):
  print('Fields of ZC_NOTIFY_STANDENTRY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_STANDENTRY3(v):
  print('Fields of ZC_NOTIFY_STANDENTRY3:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")

def print_ZC_NOTIFY_STANDENTRY4(v):
  print('Fields of ZC_NOTIFY_STANDENTRY4:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_STANDENTRY5(v):
  print('Fields of ZC_NOTIFY_STANDENTRY5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - name: {v.name}")

def print_ZC_NOTIFY_STANDENTRY7(v):
  print('Fields of ZC_NOTIFY_STANDENTRY7:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")

def print_ZC_NOTIFY_STANDENTRY8(v):
  print('Fields of ZC_NOTIFY_STANDENTRY8:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - job: {v.job}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - robe: {v.robe}")
  print(f" - GUID: {v.GUID}")
  print(f" - GEmblemVer: {v.GEmblemVer}")
  print(f" - honor: {v.honor}")
  print(f" - virtue: {v.virtue}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")
  print(f" - state: {v.state}")
  print(f" - clevel: {v.clevel}")
  print(f" - font: {v.font}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - HP: {v.HP}")
  print(f" - isBoss: {v.isBoss}")

def print_ZC_NOTIFY_STANDENTRY_NPC(v):
  print('Fields of ZC_NOTIFY_STANDENTRY_NPC:')
  print(f" - packetId: {v.packetId}")
  print(f" - objecttype: {v.objecttype}")
  print(f" - GID: {v.GID}")
  print(f" - speed: {v.speed}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - head: {v.head}")
  print(f" - weapon: {v.weapon}")
  print(f" - accessory: {v.accessory}")
  print(f" - job: {v.job}")
  print(f" - shield: {v.shield}")
  print(f" - accessory2: {v.accessory2}")
  print(f" - accessory3: {v.accessory3}")
  print(f" - headpalette: {v.headpalette}")
  print(f" - bodypalette: {v.bodypalette}")
  print(f" - headDir: {v.headDir}")
  print(f" - isPKModeON: {v.isPKModeON}")
  print(f" - sex: {v.sex}")
  print(f" - PosDir: {v.PosDir}")
  print(f" - xSize: {v.xSize}")
  print(f" - ySize: {v.ySize}")

def print_ZC_NOTIFY_STOREITEM_COUNTINFO(v):
  print('Fields of ZC_NOTIFY_STOREITEM_COUNTINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - curCount: {v.curCount}")
  print(f" - maxCount: {v.maxCount}")

def print_ZC_NOTIFY_TIME(v):
  print('Fields of ZC_NOTIFY_TIME:')
  print(f" - packetId: {v.packetId}")
  print(f" - time: {v.time}")

def print_ZC_NOTIFY_UNREADMAIL(v):
  print('Fields of ZC_NOTIFY_UNREADMAIL:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_NOTIFY_UPDATECHAR(v):
  print('Fields of ZC_NOTIFY_UPDATECHAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - Style: {v.Style}")
  print(f" - Item: {v.Item}")

def print_ZC_NOTIFY_UPDATEPLAYER(v):
  print('Fields of ZC_NOTIFY_UPDATEPLAYER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Style: {v.Style}")
  print(f" - Item: {v.Item}")

def print_ZC_NOTIFY_VANISH(v):
  print('Fields of ZC_NOTIFY_VANISH:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - type: {v.type}")

def print_ZC_NOTIFY_WEAPONITEMLIST(v):
  print('Fields of ZC_NOTIFY_WEAPONITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - weaponItemInfo: {v.weaponItemInfo}")

def print_ZC_NOTIFY_WEAPONITEMLIST_SUB(v):
  print('Fields of ZC_NOTIFY_WEAPONITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_NPCACK_ENABLE(v):
  print('Fields of ZC_NPCACK_ENABLE:')
  print(f" - packetId: {v.packetId}")

def print_ZC_NPCACK_MAPMOVE(v):
  print('Fields of ZC_NPCACK_MAPMOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - mapName: {v.mapName}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_NPCACK_SERVERMOVE(v):
  print('Fields of ZC_NPCACK_SERVERMOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - mapName: {v.mapName}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - ip: {v.ip}")
  print(f" - port: {v.port}")

def print_ZC_NPCSPRITE_CHANGE(v):
  print('Fields of ZC_NPCSPRITE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - type: {v.type}")
  print(f" - value: {v.value}")

def print_ZC_NPC_CHAT(v):
  print('Fields of ZC_NPC_CHAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - accountID: {v.accountID}")
  print(f" - color: {v.color}")
  print(f" - msg: {v.msg}")

def print_ZC_NPC_MARKET_OPEN(v):
  print('Fields of ZC_NPC_MARKET_OPEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_ZC_NPC_MARKET_PURCHASE_RESULT(v):
  print('Fields of ZC_NPC_MARKET_PURCHASE_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - IsBuyAllItems: {v.IsBuyAllItems}")

def print_ZC_NPC_SHOWEFST_UPDATE(v):
  print('Fields of ZC_NPC_SHOWEFST_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - effectState: {v.effectState}")
  print(f" - clevel: {v.clevel}")
  print(f" - showEFST: {v.showEFST}")

def print_ZC_NPROTECTGAMEGUARDCSAUTH(v):
  print('Fields of ZC_NPROTECTGAMEGUARDCSAUTH:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_ZC_OPENSTORE(v):
  print('Fields of ZC_OPENSTORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - itemcount: {v.itemcount}")

def print_ZC_OPEN_BARGAIN_SALE_TOOL(v):
  print('Fields of ZC_OPEN_BARGAIN_SALE_TOOL:')
  print(f" - packetId: {v.packetId}")

def print_ZC_OPEN_BUYING_STORE(v):
  print('Fields of ZC_OPEN_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - count: {v.count}")

def print_ZC_OPEN_EDITDLG(v):
  print('Fields of ZC_OPEN_EDITDLG:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_ZC_OPEN_EDITDLGSTR(v):
  print('Fields of ZC_OPEN_EDITDLGSTR:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_ZC_OPEN_SEARCH_STORE_INFO(v):
  print('Fields of ZC_OPEN_SEARCH_STORE_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - OpenType: {v.OpenType}")
  print(f" - SearchCntMax: {v.SearchCntMax}")

def print_ZC_OTHER_GUILD_LIST(v):
  print('Fields of ZC_OTHER_GUILD_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - guildList: {v.guildList}")

def print_ZC_OTHER_GUILD_LIST_SUB(v):
  print('Fields of ZC_OTHER_GUILD_LIST_SUB:')
  print(f" - guildname: {v.guildname}")
  print(f" - guildLevel: {v.guildLevel}")
  print(f" - guildMemberSize: {v.guildMemberSize}")
  print(f" - guildRanking: {v.guildRanking}")

def print_ZC_PARTY_BOOKING_ACK_DELETE(v):
  print('Fields of ZC_PARTY_BOOKING_ACK_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_PARTY_BOOKING_ACK_REGISTER(v):
  print('Fields of ZC_PARTY_BOOKING_ACK_REGISTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_PARTY_BOOKING_ACK_SEARCH(v):
  print('Fields of ZC_PARTY_BOOKING_ACK_SEARCH:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - IsExistMoreResult: {v.IsExistMoreResult}")
  print(f" - searchInfoList: {v.searchInfoList}")

def print_ZC_PARTY_BOOKING_ACK_SEARCH_SUB(v):
  print('Fields of ZC_PARTY_BOOKING_ACK_SEARCH_SUB:')
  print(f" - Index: {v.Index}")
  print(f" - CharName: {v.CharName}")
  print(f" - ExpireTime: {v.ExpireTime}")
  print(f" - Level: {v.Level}")
  print(f" - MapID: {v.MapID}")
  print(f" - Job: {v.Job}")

def print_ZC_PARTY_BOOKING_NOTIFY_DELETE(v):
  print('Fields of ZC_PARTY_BOOKING_NOTIFY_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_ZC_PARTY_BOOKING_NOTIFY_INSERT(v):
  print('Fields of ZC_PARTY_BOOKING_NOTIFY_INSERT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - CharName: {v.CharName}")
  print(f" - ExpireTime: {v.ExpireTime}")
  print(f" - Level: {v.Level}")
  print(f" - MapID: {v.MapID}")
  print(f" - Job1: {v.Job1}")
  print(f" - Job2: {v.Job2}")
  print(f" - Job3: {v.Job3}")
  print(f" - Job4: {v.Job4}")
  print(f" - Job5: {v.Job5}")
  print(f" - Job6: {v.Job6}")

def print_ZC_PARTY_BOOKING_NOTIFY_UPDATE(v):
  print('Fields of ZC_PARTY_BOOKING_NOTIFY_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - Job1: {v.Job1}")
  print(f" - Job2: {v.Job2}")
  print(f" - Job3: {v.Job3}")
  print(f" - Job4: {v.Job4}")
  print(f" - Job5: {v.Job5}")
  print(f" - Job6: {v.Job6}")

def print_ZC_PARTY_CONFIG(v):
  print('Fields of ZC_PARTY_CONFIG:')
  print(f" - packetId: {v.packetId}")
  print(f" - bRefuseJoinMsg: {v.bRefuseJoinMsg}")

def print_ZC_PARTY_JOIN_REQ(v):
  print('Fields of ZC_PARTY_JOIN_REQ:')
  print(f" - packetId: {v.packetId}")
  print(f" - GRID: {v.GRID}")
  print(f" - groupName: {v.groupName}")

def print_ZC_PARTY_JOIN_REQ_ACK(v):
  print('Fields of ZC_PARTY_JOIN_REQ_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - characterName: {v.characterName}")
  print(f" - answer: {v.answer}")

def print_ZC_PARTY_RECRUIT_ACK_DELETE(v):
  print('Fields of ZC_PARTY_RECRUIT_ACK_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_PARTY_RECRUIT_ACK_REGISTER(v):
  print('Fields of ZC_PARTY_RECRUIT_ACK_REGISTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_PARTY_RECRUIT_ADD_FILTERLINGLIST(v):
  print('Fields of ZC_PARTY_RECRUIT_ADD_FILTERLINGLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - CharName: {v.CharName}")

def print_ZC_PARTY_RECRUIT_CANCEL_VOLUNTEER(v):
  print('Fields of ZC_PARTY_RECRUIT_CANCEL_VOLUNTEER:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")

def print_ZC_PARTY_RECRUIT_CANCEL_VOLUNTEER_TO_PM(v):
  print('Fields of ZC_PARTY_RECRUIT_CANCEL_VOLUNTEER_TO_PM:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_PARTY_RECRUIT_FAILED_RECALL(v):
  print('Fields of ZC_PARTY_RECRUIT_FAILED_RECALL:')
  print(f" - packetId: {v.packetId}")
  print(f" - CallerAID: {v.CallerAID}")
  print(f" - Reason: {v.Reason}")

def print_ZC_PARTY_RECRUIT_NOTIFY_DELETE(v):
  print('Fields of ZC_PARTY_RECRUIT_NOTIFY_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_ZC_PARTY_RECRUIT_NOTIFY_INSERT(v):
  print('Fields of ZC_PARTY_RECRUIT_NOTIFY_INSERT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - ExpireTime: {v.ExpireTime}")
  print(f" - CharName: {v.CharName}")
  print(f" - Level: {v.Level}")
  print(f" - Notice: {v.Notice}")

def print_ZC_PARTY_RECRUIT_NOTIFY_UPDATE(v):
  print('Fields of ZC_PARTY_RECRUIT_NOTIFY_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")
  print(f" - Notice: {v.Notice}")

def print_ZC_PARTY_RECRUIT_RECALL_COST(v):
  print('Fields of ZC_PARTY_RECRUIT_RECALL_COST:')
  print(f" - packetId: {v.packetId}")
  print(f" - Money: {v.Money}")
  print(f" - mapName: {v.mapName}")

def print_ZC_PARTY_RECRUIT_REFUSE_VOLUNTEER(v):
  print('Fields of ZC_PARTY_RECRUIT_REFUSE_VOLUNTEER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Index: {v.Index}")

def print_ZC_PARTY_RECRUIT_REFUSE_VOLUNTEER_TO_PM(v):
  print('Fields of ZC_PARTY_RECRUIT_REFUSE_VOLUNTEER_TO_PM:')
  print(f" - packetId: {v.packetId}")
  print(f" - PM_AID: {v.PM_AID}")

def print_ZC_PARTY_RECRUIT_SUB_FILTERLINGLIST(v):
  print('Fields of ZC_PARTY_RECRUIT_SUB_FILTERLINGLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - CharName: {v.CharName}")

def print_ZC_PARTY_RECRUIT_VOLUNTEER_INFO(v):
  print('Fields of ZC_PARTY_RECRUIT_VOLUNTEER_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - Job: {v.Job}")
  print(f" - Level: {v.Level}")
  print(f" - CharName: {v.CharName}")

def print_ZC_PAR_CHANGE(v):
  print('Fields of ZC_PAR_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - varID: {v.varID}")
  print(f" - count: {v.count}")

def print_ZC_PAR_CHANGE_USER(v):
  print('Fields of ZC_PAR_CHANGE_USER:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - varID: {v.varID}")
  print(f" - count: {v.count}")

def print_ZC_PCBANG_EFFECT(v):
  print('Fields of ZC_PCBANG_EFFECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - ExpFactor: {v.ExpFactor}")
  print(f" - ExpFactor2: {v.ExpFactor2}")
  print(f" - DropFactor: {v.DropFactor}")

def print_ZC_PC_CASH_POINT_ITEMLIST(v):
  print('Fields of ZC_PC_CASH_POINT_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - CashPoint: {v.CashPoint}")
  print(f" - itemList: {v.itemList}")

def print_ZC_PC_CASH_POINT_ITEMLIST_SUB(v):
  print('Fields of ZC_PC_CASH_POINT_ITEMLIST_SUB:')
  print(f" - price: {v.price}")
  print(f" - discountprice: {v.discountprice}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")

def print_ZC_PC_CASH_POINT_UPDATE(v):
  print('Fields of ZC_PC_CASH_POINT_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - CashPoint: {v.CashPoint}")
  print(f" - Error: {v.Error}")

def print_ZC_PC_PURCHASE_ITEMLIST(v):
  print('Fields of ZC_PC_PURCHASE_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_PC_PURCHASE_ITEMLIST_FROMMC(v):
  print('Fields of ZC_PC_PURCHASE_ITEMLIST_FROMMC:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_PC_PURCHASE_ITEMLIST_FROMMC2(v):
  print('Fields of ZC_PC_PURCHASE_ITEMLIST_FROMMC2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - UniqueID: {v.UniqueID}")
  print(f" - itemList: {v.itemList}")

def print_ZC_PC_PURCHASE_ITEMLIST_FROMMC2_SUB(v):
  print('Fields of ZC_PC_PURCHASE_ITEMLIST_FROMMC2_SUB:')
  print(f" - price: {v.price}")
  print(f" - count: {v.count}")
  print(f" - index: {v.index}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_PC_PURCHASE_ITEMLIST_FROMMC_SUB(v):
  print('Fields of ZC_PC_PURCHASE_ITEMLIST_FROMMC_SUB:')
  print(f" - price: {v.price}")
  print(f" - count: {v.count}")
  print(f" - index: {v.index}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_PC_PURCHASE_ITEMLIST_SUB(v):
  print('Fields of ZC_PC_PURCHASE_ITEMLIST_SUB:')
  print(f" - price: {v.price}")
  print(f" - discountprice: {v.discountprice}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")

def print_ZC_PC_PURCHASE_MYITEMLIST(v):
  print('Fields of ZC_PC_PURCHASE_MYITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_PC_PURCHASE_MYITEMLIST_SUB(v):
  print('Fields of ZC_PC_PURCHASE_MYITEMLIST_SUB:')
  print(f" - price: {v.price}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_PC_PURCHASE_RESULT(v):
  print('Fields of ZC_PC_PURCHASE_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_PC_PURCHASE_RESULT_FROMMC(v):
  print('Fields of ZC_PC_PURCHASE_RESULT_FROMMC:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - curcount: {v.curcount}")
  print(f" - result: {v.result}")

def print_ZC_PC_SELL_ITEMLIST(v):
  print('Fields of ZC_PC_SELL_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_PC_SELL_ITEMLIST_SUB(v):
  print('Fields of ZC_PC_SELL_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - price: {v.price}")
  print(f" - overchargeprice: {v.overchargeprice}")

def print_ZC_PC_SELL_RESULT(v):
  print('Fields of ZC_PC_SELL_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_PERSONAL_INFOMATION(v):
  print('Fields of ZC_PERSONAL_INFOMATION:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drop: {v.Drop}")
  print(f" - PersonalInfo: {v.PersonalInfo}")

def print_ZC_PERSONAL_INFOMATION2(v):
  print('Fields of ZC_PERSONAL_INFOMATION2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drop: {v.Drop}")
  print(f" - infoList: {v.infoList}")

def print_ZC_PERSONAL_INFOMATION_CHN(v):
  print('Fields of ZC_PERSONAL_INFOMATION_CHN:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drop: {v.Drop}")
  print(f" - ActivityRate: {v.ActivityRate}")
  print(f" - infoList: {v.infoList}")

def print_ZC_PERSONAL_INFORMATION2_SUB(v):
  print('Fields of ZC_PERSONAL_INFORMATION2_SUB:')
  print(f" - InfoType: {v.InfoType}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drop: {v.Drop}")

def print_ZC_PERSONAL_INFORMATION_CHN_SUB(v):
  print('Fields of ZC_PERSONAL_INFORMATION_CHN_SUB:')
  print(f" - InfoType: {v.InfoType}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drop: {v.Drop}")

def print_ZC_PERSONAL_INFORMATION_SUB(v):
  print('Fields of ZC_PERSONAL_INFORMATION_SUB:')
  print(f" - InfoType: {v.InfoType}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drop: {v.Drop}")

def print_ZC_PETEGG_LIST(v):
  print('Fields of ZC_PETEGG_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - list: {v.list}")

def print_ZC_PETEGG_LIST_SUB(v):
  print('Fields of ZC_PETEGG_LIST_SUB:')
  print(f" - index: {v.index}")

def print_ZC_PET_ACT(v):
  print('Fields of ZC_PET_ACT:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - data: {v.data}")

def print_ZC_PET_EVOLUTION_RESULT(v):
  print('Fields of ZC_PET_EVOLUTION_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")

def print_ZC_PLAY_NPC_BGM(v):
  print('Fields of ZC_PLAY_NPC_BGM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Bgm: {v.Bgm}")

def print_ZC_POSITION_ID_NAME_INFO(v):
  print('Fields of ZC_POSITION_ID_NAME_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - positionInfo: {v.positionInfo}")

def print_ZC_POSITION_ID_NAME_INFO_SUB(v):
  print('Fields of ZC_POSITION_ID_NAME_INFO_SUB:')
  print(f" - positionID: {v.positionID}")
  print(f" - posName: {v.posName}")

def print_ZC_POSITION_INFO(v):
  print('Fields of ZC_POSITION_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - positionInfo: {v.positionInfo}")

def print_ZC_POSITION_INFO_SUB(v):
  print('Fields of ZC_POSITION_INFO_SUB:')
  print(f" - positionID: {v.positionID}")
  print(f" - right: {v.right}")
  print(f" - ranking: {v.ranking}")
  print(f" - payRate: {v.payRate}")

def print_ZC_PREMIUM_CAMPAIGN_INFO(v):
  print('Fields of ZC_PREMIUM_CAMPAIGN_INFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - Count: {v.Count}")
  print(f" - PremiumValue: {v.PremiumValue}")
  print(f" - campaignInfo: {v.campaignInfo}")

def print_ZC_PREMIUM_CAMPAIGN_INFO_SUB(v):
  print('Fields of ZC_PREMIUM_CAMPAIGN_INFO_SUB:')
  print(f" - Grade: {v.Grade}")
  print(f" - Exp: {v.Exp}")
  print(f" - Death: {v.Death}")
  print(f" - Drp: {v.Drp}")

def print_ZC_PRNPC_STATE(v):
  print('Fields of ZC_PRNPC_STATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - Winner: {v.Winner}")
  print(f" - Point: {v.Point}")

def print_ZC_PROGRESS(v):
  print('Fields of ZC_PROGRESS:')
  print(f" - packetId: {v.packetId}")
  print(f" - color: {v.color}")
  print(f" - time: {v.time}")

def print_ZC_PROGRESS_ACTOR(v):
  print('Fields of ZC_PROGRESS_ACTOR:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - color: {v.color}")
  print(f" - time: {v.time}")

def print_ZC_PROGRESS_CANCEL(v):
  print('Fields of ZC_PROGRESS_CANCEL:')
  print(f" - packetId: {v.packetId}")

def print_ZC_PROPERTY_HOMUN(v):
  print('Fields of ZC_PROPERTY_HOMUN:')
  print(f" - packetId: {v.packetId}")
  print(f" - szName: {v.szName}")
  print(f" - bModified: {v.bModified}")
  print(f" - nLevel: {v.nLevel}")
  print(f" - nFullness: {v.nFullness}")
  print(f" - nRelationship: {v.nRelationship}")
  print(f" - ITID: {v.ITID}")
  print(f" - atk: {v.atk}")
  print(f" - Matk: {v.Matk}")
  print(f" - hit: {v.hit}")
  print(f" - critical: {v.critical}")
  print(f" - def: {v._def}")
  print(f" - Mdef: {v.Mdef}")
  print(f" - flee: {v.flee}")
  print(f" - aspd: {v.aspd}")
  print(f" - hp: {v.hp}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - sp: {v.sp}")
  print(f" - maxSP: {v.maxSP}")
  print(f" - exp: {v.exp}")
  print(f" - maxEXP: {v.maxEXP}")
  print(f" - SKPoint: {v.SKPoint}")
  print(f" - ATKRange: {v.ATKRange}")

def print_ZC_PROPERTY_HOMUN_2(v):
  print('Fields of ZC_PROPERTY_HOMUN_2:')
  print(f" - packetId: {v.packetId}")
  print(f" - szName: {v.szName}")
  print(f" - bModified: {v.bModified}")
  print(f" - nLevel: {v.nLevel}")
  print(f" - nFullness: {v.nFullness}")
  print(f" - nRelationship: {v.nRelationship}")
  print(f" - ITID: {v.ITID}")
  print(f" - atk: {v.atk}")
  print(f" - Matk: {v.Matk}")
  print(f" - hit: {v.hit}")
  print(f" - critical: {v.critical}")
  print(f" - def: {v._def}")
  print(f" - Mdef: {v.Mdef}")
  print(f" - flee: {v.flee}")
  print(f" - aspd: {v.aspd}")
  print(f" - hp: {v.hp}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - sp: {v.sp}")
  print(f" - maxSP: {v.maxSP}")
  print(f" - exp: {v.exp}")
  print(f" - maxEXP: {v.maxEXP}")
  print(f" - SKPoint: {v.SKPoint}")
  print(f" - ATKRange: {v.ATKRange}")

def print_ZC_PROPERTY_MERCE(v):
  print('Fields of ZC_PROPERTY_MERCE:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")
  print(f" - level: {v.level}")
  print(f" - faith: {v.faith}")
  print(f" - summonCount: {v.summonCount}")
  print(f" - atk: {v.atk}")
  print(f" - Matk: {v.Matk}")
  print(f" - hit: {v.hit}")
  print(f" - critical: {v.critical}")
  print(f" - def: {v._def}")
  print(f" - Mdef: {v.Mdef}")
  print(f" - flee: {v.flee}")
  print(f" - aspd: {v.aspd}")
  print(f" - hp: {v.hp}")
  print(f" - maxHP: {v.maxHP}")
  print(f" - sp: {v.sp}")
  print(f" - maxSP: {v.maxSP}")
  print(f" - ATKRange: {v.ATKRange}")
  print(f" - exp: {v.exp}")

def print_ZC_PROPERTY_PET(v):
  print('Fields of ZC_PROPERTY_PET:')
  print(f" - packetId: {v.packetId}")
  print(f" - szName: {v.szName}")
  print(f" - bModified: {v.bModified}")
  print(f" - nLevel: {v.nLevel}")
  print(f" - nFullness: {v.nFullness}")
  print(f" - nRelationship: {v.nRelationship}")
  print(f" - ITID: {v.ITID}")
  print(f" - job: {v.job}")

def print_ZC_QUEST_NOTIFY_EFFECT(v):
  print('Fields of ZC_QUEST_NOTIFY_EFFECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - npcID: {v.npcID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - effect: {v.effect}")
  print(f" - type: {v.type}")

def print_ZC_READ_BOOK(v):
  print('Fields of ZC_READ_BOOK:')
  print(f" - packetId: {v.packetId}")
  print(f" - bookID: {v.bookID}")
  print(f" - page: {v.page}")

def print_ZC_RECOVERY(v):
  print('Fields of ZC_RECOVERY:')
  print(f" - packetId: {v.packetId}")
  print(f" - varID: {v.varID}")
  print(f" - amount: {v.amount}")

def print_ZC_RECOVERY2(v):
  print('Fields of ZC_RECOVERY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - varID: {v.varID}")
  print(f" - amount: {v.amount}")

def print_ZC_RECV_ROULETTE_ITEM(v):
  print('Fields of ZC_RECV_ROULETTE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - AdditionItemID: {v.AdditionItemID}")

def print_ZC_REFUSE_ENTER(v):
  print('Fields of ZC_REFUSE_ENTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - ErrorCode: {v.ErrorCode}")

def print_ZC_REFUSE_ENTER_ROOM(v):
  print('Fields of ZC_REFUSE_ENTER_ROOM:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_REFUSE_QUIT(v):
  print('Fields of ZC_REFUSE_QUIT:')
  print(f" - packetId: {v.packetId}")

def print_ZC_REPAIRITEMLIST(v):
  print('Fields of ZC_REPAIRITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_REPAIRITEMLIST_SUB(v):
  print('Fields of ZC_REPAIRITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_REPLY_ACK_ENTRY_QUEUE_ADMISSION(v):
  print('Fields of ZC_REPLY_ACK_ENTRY_QUEUE_ADMISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - EntryQueueName: {v.EntryQueueName}")

def print_ZC_REPLY_ACK_LOBBY_ADMISSION(v):
  print('Fields of ZC_REPLY_ACK_LOBBY_ADMISSION:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - EntryQueueName: {v.EntryQueueName}")
  print(f" - LobbyName: {v.LobbyName}")

def print_ZC_REPLY_REMAINTIME(v):
  print('Fields of ZC_REPLY_REMAINTIME:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - ExpirationDate: {v.ExpirationDate}")
  print(f" - RemainTime: {v.RemainTime}")

def print_ZC_REQ_ACH_REWARD_ACK(v):
  print('Fields of ZC_REQ_ACH_REWARD_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")
  print(f" - ACHID: {v.ACHID}")

def print_ZC_REQ_ADD_FRIENDS(v):
  print('Fields of ZC_REQ_ADD_FRIENDS:')
  print(f" - packetId: {v.packetId}")
  print(f" - ReqAID: {v.ReqAID}")
  print(f" - ReqGID: {v.ReqGID}")
  print(f" - Name: {v.Name}")

def print_ZC_REQ_ALLY_GUILD(v):
  print('Fields of ZC_REQ_ALLY_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - otherAID: {v.otherAID}")
  print(f" - guildName: {v.guildName}")

def print_ZC_REQ_AU_BOT(v):
  print('Fields of ZC_REQ_AU_BOT:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

def print_ZC_REQ_BABY(v):
  print('Fields of ZC_REQ_BABY:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - name: {v.name}")

def print_ZC_REQ_CASH_PASSWORD(v):
  print('Fields of ZC_REQ_CASH_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Info: {v.Info}")

def print_ZC_REQ_COUPLE(v):
  print('Fields of ZC_REQ_COUPLE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - name: {v.name}")

def print_ZC_REQ_EXCHANGE_ITEM(v):
  print('Fields of ZC_REQ_EXCHANGE_ITEM:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")

def print_ZC_REQ_EXCHANGE_ITEM2(v):
  print('Fields of ZC_REQ_EXCHANGE_ITEM2:')
  print(f" - packetId: {v.packetId}")
  print(f" - name: {v.name}")
  print(f" - GID: {v.GID}")
  print(f" - level: {v.level}")

def print_ZC_REQ_GROUPINFO_CHANGE_V2(v):
  print('Fields of ZC_REQ_GROUPINFO_CHANGE_V2:')
  print(f" - packetId: {v.packetId}")
  print(f" - expOption: {v.expOption}")
  print(f" - ItemPickupRule: {v.ItemPickupRule}")
  print(f" - ItemDivisionRule: {v.ItemDivisionRule}")

def print_ZC_REQ_JOIN_GROUP(v):
  print('Fields of ZC_REQ_JOIN_GROUP:')
  print(f" - packetId: {v.packetId}")
  print(f" - GRID: {v.GRID}")
  print(f" - groupName: {v.groupName}")

def print_ZC_REQ_JOIN_GUILD(v):
  print('Fields of ZC_REQ_JOIN_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - guildName: {v.guildName}")

def print_ZC_REQ_STORE_PASSWORD(v):
  print('Fields of ZC_REQ_STORE_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Info: {v.Info}")

def print_ZC_REQ_TAKEOFF_EQUIP_ACK(v):
  print('Fields of ZC_REQ_TAKEOFF_EQUIP_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - result: {v.result}")

def print_ZC_REQ_TAKEOFF_EQUIP_ACK2(v):
  print('Fields of ZC_REQ_TAKEOFF_EQUIP_ACK2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - result: {v.result}")

def print_ZC_REQ_WEAR_EQUIP_ACK(v):
  print('Fields of ZC_REQ_WEAR_EQUIP_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - result: {v.result}")

def print_ZC_REQ_WEAR_EQUIP_ACK2(v):
  print('Fields of ZC_REQ_WEAR_EQUIP_ACK2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - wearLocation: {v.wearLocation}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - result: {v.result}")

def print_ZC_RESTART_ACK(v):
  print('Fields of ZC_RESTART_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")

def print_ZC_RESULT_CASH_PASSWORD(v):
  print('Fields of ZC_RESULT_CASH_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - ErrorCount: {v.ErrorCount}")

def print_ZC_RESULT_MAKE_GUILD(v):
  print('Fields of ZC_RESULT_MAKE_GUILD:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_RESULT_STORE_PASSWORD(v):
  print('Fields of ZC_RESULT_STORE_PASSWORD:')
  print(f" - packetId: {v.packetId}")
  print(f" - Result: {v.Result}")
  print(f" - ErrorCount: {v.ErrorCount}")

def print_ZC_RESURRECTION(v):
  print('Fields of ZC_RESURRECTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - type: {v.type}")

def print_ZC_ROLE_CHANGE(v):
  print('Fields of ZC_ROLE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - role: {v.role}")
  print(f" - name: {v.name}")

def print_ZC_ROOM_NEWENTRY(v):
  print('Fields of ZC_ROOM_NEWENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - roomID: {v.roomID}")
  print(f" - maxcount: {v.maxcount}")
  print(f" - curcount: {v.curcount}")
  print(f" - type: {v.type}")
  print(f" - title: {v.title}")

def print_ZC_SAY_DIALOG(v):
  print('Fields of ZC_SAY_DIALOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - NAID: {v.NAID}")
  print(f" - msg: {v.msg}")

def print_ZC_SEARCH_STORE_INFO_ACK(v):
  print('Fields of ZC_SEARCH_STORE_INFO_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - IsFirstPage: {v.IsFirstPage}")
  print(f" - IsNexPage: {v.IsNexPage}")
  print(f" - RemainedSearchCnt: {v.RemainedSearchCnt}")
  print(f" - SSI_List: {v.SSI_List}")

def print_ZC_SEARCH_STORE_INFO_ACK_LIST(v):
  print('Fields of ZC_SEARCH_STORE_INFO_ACK_LIST:')
  print(f" - SSI_ID: {v.SSI_ID}")
  print(f" - AID: {v.AID}")
  print(f" - StoreName: {v.StoreName}")
  print(f" - ITID: {v.ITID}")
  print(f" - ItemType: {v.ItemType}")
  print(f" - price: {v.price}")
  print(f" - count: {v.count}")
  print(f" - refiningLevel: {v.refiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_SEARCH_STORE_INFO_FAILED(v):
  print('Fields of ZC_SEARCH_STORE_INFO_FAILED:')
  print(f" - packetId: {v.packetId}")
  print(f" - Reason: {v.Reason}")

def print_ZC_SEARCH_STORE_OPEN_INFO(v):
  print('Fields of ZC_SEARCH_STORE_OPEN_INFO:')
  print(f" - packetId: {v.packetId}")

def print_ZC_SECRETSCAN_DATA(v):
  print('Fields of ZC_SECRETSCAN_DATA:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")

def print_ZC_SEEK_PARTY(v):
  print('Fields of ZC_SEEK_PARTY:')
  print(f" - packetId: {v.packetId}")
  print(f" - Name: {v.Name}")
  print(f" - Job: {v.Job}")
  print(f" - Level: {v.Level}")
  print(f" - mapName: {v.mapName}")
  print(f" - Option: {v.Option}")

def print_ZC_SEEK_PARTY_MEMBER(v):
  print('Fields of ZC_SEEK_PARTY_MEMBER:')
  print(f" - packetId: {v.packetId}")
  print(f" - Name: {v.Name}")
  print(f" - Job: {v.Job}")
  print(f" - Level: {v.Level}")
  print(f" - mapName: {v.mapName}")
  print(f" - Option: {v.Option}")

def print_ZC_SELECT_DEALTYPE(v):
  print('Fields of ZC_SELECT_DEALTYPE:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_ZC_SETTING_WHISPER_PC(v):
  print('Fields of ZC_SETTING_WHISPER_PC:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")

def print_ZC_SETTING_WHISPER_STATE(v):
  print('Fields of ZC_SETTING_WHISPER_STATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - result: {v.result}")

def print_ZC_SE_CASHSHOP_OPEN(v):
  print('Fields of ZC_SE_CASHSHOP_OPEN:')
  print(f" - packetId: {v.packetId}")
  print(f" - cash_point: {v.cash_point}")

def print_ZC_SE_CASHSHOP_UPDATE(v):
  print('Fields of ZC_SE_CASHSHOP_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - cash_point: {v.cash_point}")
  print(f" - free_point: {v.free_point}")

def print_ZC_SE_PC_BUY_CASHITEM_RESULT(v):
  print('Fields of ZC_SE_PC_BUY_CASHITEM_RESULT:')
  print(f" - packetId: {v.packetId}")
  print(f" - item_id: {v.item_id}")
  print(f" - result: {v.result}")

def print_ZC_SHANDA_PROTECT(v):
  print('Fields of ZC_SHANDA_PROTECT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - CodeLen: {v.CodeLen}")
  print(f" - Code: {v.Code}")

def print_ZC_SHORTCUT_KEY_LIST(v):
  print('Fields of ZC_SHORTCUT_KEY_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - keyList: {v.keyList}")

def print_ZC_SHORTCUT_KEY_LIST_SUB(v):
  print('Fields of ZC_SHORTCUT_KEY_LIST_SUB:')
  print(f" - isSkill: {v.isSkill}")
  print(f" - ID: {v.ID}")
  print(f" - count: {v.count}")

def print_ZC_SHORTCUT_KEY_LIST_V2(v):
  print('Fields of ZC_SHORTCUT_KEY_LIST_V2:')
  print(f" - packetId: {v.packetId}")
  print(f" - keyList: {v.keyList}")

def print_ZC_SHORTCUT_KEY_LIST_V2_SUB(v):
  print('Fields of ZC_SHORTCUT_KEY_LIST_V2_SUB:')
  print(f" - isSkill: {v.isSkill}")
  print(f" - ID: {v.ID}")
  print(f" - count: {v.count}")

def print_ZC_SHORTCUT_KEY_LIST_V3(v):
  print('Fields of ZC_SHORTCUT_KEY_LIST_V3:')
  print(f" - packetId: {v.packetId}")
  print(f" - Rotate: {v.Rotate}")
  print(f" - keys: {v.keys}")

def print_ZC_SHORTCUT_KEY_LIST_V3_KEYS(v):
  print('Fields of ZC_SHORTCUT_KEY_LIST_V3_KEYS:')
  print(f" - isSkill: {v.isSkill}")
  print(f" - ID: {v.ID}")
  print(f" - count: {v.count}")

def print_ZC_SHOWDIGIT(v):
  print('Fields of ZC_SHOWDIGIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - type: {v.type}")
  print(f" - value: {v.value}")

def print_ZC_SHOW_IMAGE(v):
  print('Fields of ZC_SHOW_IMAGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - imageName: {v.imageName}")
  print(f" - type: {v.type}")

def print_ZC_SHOW_IMAGE2(v):
  print('Fields of ZC_SHOW_IMAGE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - imageName: {v.imageName}")
  print(f" - type: {v.type}")

def print_ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST(v):
  print('Fields of ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - CashPoint: {v.CashPoint}")
  print(f" - md_itemcount: {v.md_itemcount}")
  print(f" - md_itemSize: {v.md_itemSize}")
  print(f" - best_itemcount: {v.best_itemcount}")
  print(f" - best_itemsize: {v.best_itemsize}")
  print(f" - md_item: {v.md_item}")

def print_ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST_ITEM(v):
  print('Fields of ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST_ITEM:')
  print(f" - price: {v.price}")
  print(f" - discountprice: {v.discountprice}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")

def print_ZC_SIMPLE_CASH_BTNSHOW(v):
  print('Fields of ZC_SIMPLE_CASH_BTNSHOW:')
  print(f" - packetId: {v.packetId}")
  print(f" - show: {v.show}")

def print_ZC_SIMPLE_CASH_POINT_ITEMLIST(v):
  print('Fields of ZC_SIMPLE_CASH_POINT_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - CashPoint: {v.CashPoint}")
  print(f" - itemList: {v.itemList}")

def print_ZC_SIMPLE_CASH_POINT_ITEMLIST_SUB(v):
  print('Fields of ZC_SIMPLE_CASH_POINT_ITEMLIST_SUB:')
  print(f" - price: {v.price}")
  print(f" - discountprice: {v.discountprice}")
  print(f" - type: {v.type}")
  print(f" - ITID: {v.ITID}")

def print_ZC_SKILLINFO_DELETE(v):
  print('Fields of ZC_SKILLINFO_DELETE:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")

def print_ZC_SKILLINFO_LIST(v):
  print('Fields of ZC_SKILLINFO_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - skillList: {v.skillList}")

def print_ZC_SKILLINFO_LIST_SUB(v):
  print('Fields of ZC_SKILLINFO_LIST_SUB:')
  print(f" - SKID: {v.SKID}")
  print(f" - type: {v.type}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - skillName: {v.skillName}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_SKILLINFO_UPDATE(v):
  print('Fields of ZC_SKILLINFO_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_SKILLINFO_UPDATE2(v):
  print('Fields of ZC_SKILLINFO_UPDATE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - type: {v.type}")
  print(f" - level: {v.level}")
  print(f" - spcost: {v.spcost}")
  print(f" - attackRange: {v.attackRange}")
  print(f" - upgradable: {v.upgradable}")

def print_ZC_SKILLMSG(v):
  print('Fields of ZC_SKILLMSG:')
  print(f" - packetId: {v.packetId}")
  print(f" - MsgNo: {v.MsgNo}")

def print_ZC_SKILL_DISAPPEAR(v):
  print('Fields of ZC_SKILL_DISAPPEAR:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_SKILL_ENTRY(v):
  print('Fields of ZC_SKILL_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - creatorAID: {v.creatorAID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - job: {v.job}")
  print(f" - isVisible: {v.isVisible}")

def print_ZC_SKILL_ENTRY2(v):
  print('Fields of ZC_SKILL_ENTRY2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - creatorAID: {v.creatorAID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - job: {v.job}")
  print(f" - isVisible: {v.isVisible}")
  print(f" - isContens: {v.isContens}")
  print(f" - msg: {v.msg}")

def print_ZC_SKILL_ENTRY3(v):
  print('Fields of ZC_SKILL_ENTRY3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - creatorAID: {v.creatorAID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - job: {v.job}")
  print(f" - RadiusRange: {v.RadiusRange}")
  print(f" - isVisible: {v.isVisible}")

def print_ZC_SKILL_ENTRY4(v):
  print('Fields of ZC_SKILL_ENTRY4:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - creatorAID: {v.creatorAID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - job: {v.job}")
  print(f" - RadiusRange: {v.RadiusRange}")
  print(f" - isVisible: {v.isVisible}")

def print_ZC_SKILL_ENTRY5(v):
  print('Fields of ZC_SKILL_ENTRY5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - AID: {v.AID}")
  print(f" - creatorAID: {v.creatorAID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - job: {v.job}")
  print(f" - RadiusRange: {v.RadiusRange}")
  print(f" - isVisible: {v.isVisible}")
  print(f" - level: {v.level}")

def print_ZC_SKILL_POSTDELAY(v):
  print('Fields of ZC_SKILL_POSTDELAY:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - DelayTM: {v.DelayTM}")

def print_ZC_SKILL_POSTDELAY_LIST(v):
  print('Fields of ZC_SKILL_POSTDELAY_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - skillList: {v.skillList}")

def print_ZC_SKILL_POSTDELAY_LIST2(v):
  print('Fields of ZC_SKILL_POSTDELAY_LIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - skillList: {v.skillList}")

def print_ZC_SKILL_POSTDELAY_LIST2_SUB(v):
  print('Fields of ZC_SKILL_POSTDELAY_LIST2_SUB:')
  print(f" - SKID: {v.SKID}")
  print(f" - MaxDelayTM: {v.MaxDelayTM}")
  print(f" - DelayTM: {v.DelayTM}")

def print_ZC_SKILL_POSTDELAY_LIST_SUB(v):
  print('Fields of ZC_SKILL_POSTDELAY_LIST_SUB:')
  print(f" - SKID: {v.SKID}")
  print(f" - DelayTM: {v.DelayTM}")

def print_ZC_SKILL_SELECT_REQUEST(v):
  print('Fields of ZC_SKILL_SELECT_REQUEST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - why: {v.why}")
  print(f" - SKIDList: {v.SKIDList}")

def print_ZC_SKILL_UPDATE(v):
  print('Fields of ZC_SKILL_UPDATE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")

def print_ZC_SOUND(v):
  print('Fields of ZC_SOUND:')
  print(f" - packetId: {v.packetId}")
  print(f" - fileName: {v.fileName}")
  print(f" - act: {v.act}")
  print(f" - term: {v.term}")
  print(f" - NAID: {v.NAID}")

def print_ZC_SPIRITS(v):
  print('Fields of ZC_SPIRITS:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - num: {v.num}")

def print_ZC_SPIRITS2(v):
  print('Fields of ZC_SPIRITS2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - num: {v.num}")

def print_ZC_SPIRITS_ATTRIBUTE(v):
  print('Fields of ZC_SPIRITS_ATTRIBUTE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - SpritsType: {v.SpritsType}")
  print(f" - Num: {v.Num}")

def print_ZC_SPRITE_CHANGE(v):
  print('Fields of ZC_SPRITE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - type: {v.type}")
  print(f" - value: {v.value}")

def print_ZC_SPRITE_CHANGE2(v):
  print('Fields of ZC_SPRITE_CHANGE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")
  print(f" - type: {v.type}")
  print(f" - value: {v.value}")

def print_ZC_SRPACKETR2_INIT(v):
  print('Fields of ZC_SRPACKETR2_INIT:')
  print(f" - packetId: {v.packetId}")
  print(f" - ProtectFactor: {v.ProtectFactor}")
  print(f" - DeformSeedFactor: {v.DeformSeedFactor}")
  print(f" - DeformAddFactor: {v.DeformAddFactor}")

def print_ZC_SSILIST_ITEM_CLICK_ACK(v):
  print('Fields of ZC_SSILIST_ITEM_CLICK_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - x: {v.x}")
  print(f" - y: {v.y}")

def print_ZC_STARPLACE(v):
  print('Fields of ZC_STARPLACE:')
  print(f" - packetId: {v.packetId}")
  print(f" - which: {v.which}")

def print_ZC_STARSKILL(v):
  print('Fields of ZC_STARSKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - mapName: {v.mapName}")
  print(f" - monsterID: {v.monsterID}")
  print(f" - star: {v.star}")
  print(f" - result: {v.result}")

def print_ZC_START_BABY(v):
  print('Fields of ZC_START_BABY:')
  print(f" - packetId: {v.packetId}")

def print_ZC_START_CAPTURE(v):
  print('Fields of ZC_START_CAPTURE:')
  print(f" - packetId: {v.packetId}")

def print_ZC_START_COLLECTION(v):
  print('Fields of ZC_START_COLLECTION:')
  print(f" - packetId: {v.packetId}")

def print_ZC_START_COUPLE(v):
  print('Fields of ZC_START_COUPLE:')
  print(f" - packetId: {v.packetId}")

def print_ZC_STATE_CHANGE(v):
  print('Fields of ZC_STATE_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - isPKModeON: {v.isPKModeON}")

def print_ZC_STATE_CHANGE3(v):
  print('Fields of ZC_STATE_CHANGE3:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - bodyState: {v.bodyState}")
  print(f" - healthState: {v.healthState}")
  print(f" - effectState: {v.effectState}")
  print(f" - isPKModeON: {v.isPKModeON}")

def print_ZC_STATUS(v):
  print('Fields of ZC_STATUS:')
  print(f" - packetId: {v.packetId}")
  print(f" - point: {v.point}")
  print(f" - str: {v.str}")
  print(f" - standardStr: {v.standardStr}")
  print(f" - agi: {v.agi}")
  print(f" - standardAgi: {v.standardAgi}")
  print(f" - vit: {v.vit}")
  print(f" - standardVit: {v.standardVit}")
  print(f" - Int: {v.Int}")
  print(f" - standardInt: {v.standardInt}")
  print(f" - dex: {v.dex}")
  print(f" - standardDex: {v.standardDex}")
  print(f" - luk: {v.luk}")
  print(f" - standardLuk: {v.standardLuk}")
  print(f" - attPower: {v.attPower}")
  print(f" - refiningPower: {v.refiningPower}")
  print(f" - max_mattPower: {v.max_mattPower}")
  print(f" - min_mattPower: {v.min_mattPower}")
  print(f" - itemdefPower: {v.itemdefPower}")
  print(f" - plusdefPower: {v.plusdefPower}")
  print(f" - mdefPower: {v.mdefPower}")
  print(f" - plusmdefPower: {v.plusmdefPower}")
  print(f" - hitSuccessValue: {v.hitSuccessValue}")
  print(f" - avoidSuccessValue: {v.avoidSuccessValue}")
  print(f" - plusAvoidSuccessValue: {v.plusAvoidSuccessValue}")
  print(f" - criticalSuccessValue: {v.criticalSuccessValue}")
  print(f" - ASPD: {v.ASPD}")
  print(f" - plusASPD: {v.plusASPD}")

def print_ZC_STATUS_CHANGE(v):
  print('Fields of ZC_STATUS_CHANGE:')
  print(f" - packetId: {v.packetId}")
  print(f" - statusID: {v.statusID}")
  print(f" - value: {v.value}")

def print_ZC_STATUS_CHANGE_ACK(v):
  print('Fields of ZC_STATUS_CHANGE_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - statusID: {v.statusID}")
  print(f" - result: {v.result}")
  print(f" - value: {v.value}")

def print_ZC_STOPMOVE(v):
  print('Fields of ZC_STOPMOVE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_STOPMOVE_FORCE(v):
  print('Fields of ZC_STOPMOVE_FORCE:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")

def print_ZC_STORE_ENTRY(v):
  print('Fields of ZC_STORE_ENTRY:')
  print(f" - packetId: {v.packetId}")
  print(f" - makerAID: {v.makerAID}")
  print(f" - storeName: {v.storeName}")

def print_ZC_STORE_EQUIPMENT_ITEMLIST(v):
  print('Fields of ZC_STORE_EQUIPMENT_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_STORE_EQUIPMENT_ITEMLIST2(v):
  print('Fields of ZC_STORE_EQUIPMENT_ITEMLIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_STORE_EQUIPMENT_ITEMLIST2_SUB(v):
  print('Fields of ZC_STORE_EQUIPMENT_ITEMLIST2_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_STORE_EQUIPMENT_ITEMLIST3(v):
  print('Fields of ZC_STORE_EQUIPMENT_ITEMLIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - equipmentList: {v.equipmentList}")

def print_ZC_STORE_EQUIPMENT_ITEMLIST3_SUB(v):
  print('Fields of ZC_STORE_EQUIPMENT_ITEMLIST3_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")

def print_ZC_STORE_EQUIPMENT_ITEMLIST_SUB(v):
  print('Fields of ZC_STORE_EQUIPMENT_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - IsDamaged: {v.IsDamaged}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_STORE_ITEMLIST_EQUIP_V5(v):
  print('Fields of ZC_STORE_ITEMLIST_EQUIP_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_STORE_ITEMLIST_EQUIP_V5_ITEMINFO(v):
  print('Fields of ZC_STORE_ITEMLIST_EQUIP_V5_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - location: {v.location}")
  print(f" - WearState: {v.WearState}")
  print(f" - RefiningLevel: {v.RefiningLevel}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - bindOnEquipType: {v.bindOnEquipType}")
  print(f" - wItemSpriteNumber: {v.wItemSpriteNumber}")
  print(f" - Flag: {v.Flag}")

def print_ZC_STORE_ITEMLIST_EQUIP_V6(v):
  print('Fields of ZC_STORE_ITEMLIST_EQUIP_V6:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - StoreName: {v.StoreName}")

def print_ZC_STORE_ITEMLIST_NORMAL_V5(v):
  print('Fields of ZC_STORE_ITEMLIST_NORMAL_V5:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_STORE_ITEMLIST_NORMAL_V5_ITEMINFO(v):
  print('Fields of ZC_STORE_ITEMLIST_NORMAL_V5_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")
  print(f" - Flag: {v.Flag}")

def print_ZC_STORE_NORMAL_ITEMLIST(v):
  print('Fields of ZC_STORE_NORMAL_ITEMLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemInfo: {v.itemInfo}")

def print_ZC_STORE_NORMAL_ITEMLIST2(v):
  print('Fields of ZC_STORE_NORMAL_ITEMLIST2:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - itemList: {v.itemList}")

def print_ZC_STORE_NORMAL_ITEMLIST2_SUB(v):
  print('Fields of ZC_STORE_NORMAL_ITEMLIST2_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")

def print_ZC_STORE_NORMAL_ITEMLIST3(v):
  print('Fields of ZC_STORE_NORMAL_ITEMLIST3:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - ItemInfo: {v.ItemInfo}")

def print_ZC_STORE_NORMAL_ITEMLIST3_ITEMINFO(v):
  print('Fields of ZC_STORE_NORMAL_ITEMLIST3_ITEMINFO:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")
  print(f" - card1: {v.card1}")
  print(f" - card2: {v.card2}")
  print(f" - card3: {v.card3}")
  print(f" - card4: {v.card4}")
  print(f" - HireExpireDate: {v.HireExpireDate}")

def print_ZC_STORE_NORMAL_ITEMLIST_SUB(v):
  print('Fields of ZC_STORE_NORMAL_ITEMLIST_SUB:')
  print(f" - index: {v.index}")
  print(f" - ITID: {v.ITID}")
  print(f" - type: {v.type}")
  print(f" - IsIdentified: {v.IsIdentified}")
  print(f" - count: {v.count}")
  print(f" - WearState: {v.WearState}")

def print_ZC_TAEKWON_POINT(v):
  print('Fields of ZC_TAEKWON_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - Point: {v.Point}")
  print(f" - TotalPoint: {v.TotalPoint}")

def print_ZC_TAEKWON_RANK(v):
  print('Fields of ZC_TAEKWON_RANK:')
  print(f" - packetId: {v.packetId}")
  print(f" - Name: {v.Name}")
  print(f" - Point: {v.Point}")

def print_ZC_TALKBOX_CHATCONTENTS(v):
  print('Fields of ZC_TALKBOX_CHATCONTENTS:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - contents: {v.contents}")

def print_ZC_THROW_MVPITEM(v):
  print('Fields of ZC_THROW_MVPITEM:')
  print(f" - packetId: {v.packetId}")

def print_ZC_TRYCAPTURE_MONSTER(v):
  print('Fields of ZC_TRYCAPTURE_MONSTER:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_TRYCOLLECTION(v):
  print('Fields of ZC_TRYCOLLECTION:')
  print(f" - packetId: {v.packetId}")
  print(f" - result: {v.result}")

def print_ZC_UPDATE_CHARSTAT(v):
  print('Fields of ZC_UPDATE_CHARSTAT:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - status: {v.status}")

def print_ZC_UPDATE_CHARSTAT2(v):
  print('Fields of ZC_UPDATE_CHARSTAT2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - GID: {v.GID}")
  print(f" - status: {v.status}")
  print(f" - sex: {v.sex}")
  print(f" - head: {v.head}")
  print(f" - headPalette: {v.headPalette}")

def print_ZC_UPDATE_GDID(v):
  print('Fields of ZC_UPDATE_GDID:')
  print(f" - packetId: {v.packetId}")
  print(f" - GDID: {v.GDID}")
  print(f" - emblemVersion: {v.emblemVersion}")
  print(f" - right: {v.right}")
  print(f" - isMaster: {v.isMaster}")
  print(f" - InterSID: {v.InterSID}")
  print(f" - GName: {v.GName}")

def print_ZC_UPDATE_ITEM_FROM_BUYING_STORE(v):
  print('Fields of ZC_UPDATE_ITEM_FROM_BUYING_STORE:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - count: {v.count}")
  print(f" - limitZeny: {v.limitZeny}")

def print_ZC_UPDATE_ITEM_FROM_BUYING_STORE2(v):
  print('Fields of ZC_UPDATE_ITEM_FROM_BUYING_STORE2:')
  print(f" - packetId: {v.packetId}")
  print(f" - ITID: {v.ITID}")
  print(f" - count: {v.count}")
  print(f" - Zeny: {v.Zeny}")
  print(f" - limitZeny: {v.limitZeny}")
  print(f" - FromGID: {v.FromGID}")
  print(f" - Date: {v.Date}")

def print_ZC_UPDATE_MAPINFO(v):
  print('Fields of ZC_UPDATE_MAPINFO:')
  print(f" - packetId: {v.packetId}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - type: {v.type}")
  print(f" - mapName: {v.mapName}")

def print_ZC_UPDATE_MISSION_HUNT(v):
  print('Fields of ZC_UPDATE_MISSION_HUNT:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - count: {v.count}")
  print(f" - mobList: {v.mobList}")

def print_ZC_UPDATE_MISSION_HUNT_EX(v):
  print('Fields of ZC_UPDATE_MISSION_HUNT_EX:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - count: {v.count}")

def print_ZC_UPDATE_MISSION_HUNT_SUB(v):
  print('Fields of ZC_UPDATE_MISSION_HUNT_SUB:')
  print(f" - questID: {v.questID}")
  print(f" - mobGID: {v.mobGID}")
  print(f" - maxCount: {v.maxCount}")
  print(f" - count: {v.count}")

def print_ZC_UPDATE_RANKING_POINT(v):
  print('Fields of ZC_UPDATE_RANKING_POINT:')
  print(f" - packetId: {v.packetId}")
  print(f" - RankingType: {v.RankingType}")
  print(f" - Point: {v.Point}")
  print(f" - TotalPoint: {v.TotalPoint}")

def print_ZC_USER_COUNT(v):
  print('Fields of ZC_USER_COUNT:')
  print(f" - packetId: {v.packetId}")
  print(f" - count: {v.count}")

def print_ZC_USESKILL_ACK(v):
  print('Fields of ZC_USESKILL_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - targetID: {v.targetID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - SKID: {v.SKID}")
  print(f" - property: {v.property}")
  print(f" - delayTime: {v.delayTime}")

def print_ZC_USESKILL_ACK2(v):
  print('Fields of ZC_USESKILL_ACK2:')
  print(f" - packetId: {v.packetId}")
  print(f" - AID: {v.AID}")
  print(f" - targetID: {v.targetID}")
  print(f" - xPos: {v.xPos}")
  print(f" - yPos: {v.yPos}")
  print(f" - SKID: {v.SKID}")
  print(f" - property: {v.property}")
  print(f" - delayTime: {v.delayTime}")
  print(f" - isDisposable: {v.isDisposable}")

def print_ZC_USE_ITEM_ACK(v):
  print('Fields of ZC_USE_ITEM_ACK:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - count: {v.count}")
  print(f" - result: {v.result}")

def print_ZC_USE_ITEM_ACK2(v):
  print('Fields of ZC_USE_ITEM_ACK2:')
  print(f" - packetId: {v.packetId}")
  print(f" - index: {v.index}")
  print(f" - id: {v.id}")
  print(f" - AID: {v.AID}")
  print(f" - count: {v.count}")
  print(f" - result: {v.result}")

def print_ZC_USE_SKILL(v):
  print('Fields of ZC_USE_SKILL:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - level: {v.level}")
  print(f" - targetAID: {v.targetAID}")
  print(f" - srcAID: {v.srcAID}")
  print(f" - result: {v.result}")

def print_ZC_USE_SKILL2(v):
  print('Fields of ZC_USE_SKILL2:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - level: {v.level}")
  print(f" - targetAID: {v.targetAID}")
  print(f" - srcAID: {v.srcAID}")
  print(f" - result: {v.result}")

def print_ZC_WAIT_DIALOG(v):
  print('Fields of ZC_WAIT_DIALOG:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")

def print_ZC_WAIT_DIALOG2(v):
  print('Fields of ZC_WAIT_DIALOG2:')
  print(f" - packetId: {v.packetId}")
  print(f" - NAID: {v.NAID}")
  print(f" - type: {v.type}")

def print_ZC_WARPLIST(v):
  print('Fields of ZC_WARPLIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - SKID: {v.SKID}")
  print(f" - mapName: {v.mapName}")

def print_ZC_WHISPER(v):
  print('Fields of ZC_WHISPER:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - sender: {v.sender}")
  print(f" - msg: {v.msg}")

def print_ZC_WHISPER02(v):
  print('Fields of ZC_WHISPER02:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - senderGID: {v.senderGID}")
  print(f" - sender: {v.sender}")
  print(f" - isAdmin: {v.isAdmin}")

def print_ZC_WHISPER_LIST(v):
  print('Fields of ZC_WHISPER_LIST:')
  print(f" - packetId: {v.packetId}")
  print(f" - PacketLength: {v.PacketLength}")
  print(f" - nameList: {v.nameList}")

def print_ZC_WHISPER_LIST_SUB(v):
  print('Fields of ZC_WHISPER_LIST_SUB:')
  print(f" - name: {v.name}")

def print_ZH_MOVE_PVPWORLD(v):
  print('Fields of ZH_MOVE_PVPWORLD:')
  print(f" - packetId: {v.packetId}")
  print(f" - GID: {v.GID}")

