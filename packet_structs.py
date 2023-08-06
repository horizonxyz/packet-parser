import ctypes

# packet 0x64
class CA_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('Passwd', ctypes.c_char * 24),
		('clienttype', ctypes.c_uint8)
	]


# packet 0x65
class CH_ENTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('AuthCode', ctypes.c_uint32),
		('userLevel', ctypes.c_uint32),
		('clientType', ctypes.c_uint16),
		('Sex', ctypes.c_uint8)
	]


# packet 0x66
class CH_SELECT_CHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CharNum', ctypes.c_uint8)
	]


# packet 0x67
class CH_MAKE_CHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('Str', ctypes.c_uint8),
		('Agi', ctypes.c_uint8),
		('Vit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('Dex', ctypes.c_uint8),
		('Luk', ctypes.c_uint8),
		('CharNum', ctypes.c_uint8),
		('headPal', ctypes.c_uint16),
		('head', ctypes.c_uint16)
	]


# packet 0x68
class CH_DELETE_CHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('key', ctypes.c_char * 40)
	]


class AC_ACCEPT_LOGIN_SUB(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),	
		('ip', ctypes.c_uint32),
		('port', ctypes.c_uint16),
		('name', ctypes.c_char * 20),
		('usercount', ctypes.c_uint16),
		('state', ctypes.c_uint16),
		('property', ctypes.c_uint16),
    ]
	
# packet 0x69
class AC_ACCEPT_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AuthCode', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('userLevel', ctypes.c_uint32),
		('lastLoginIP', ctypes.c_uint32),
		('lastLoginTime', ctypes.c_char * 26),
		('Sex', ctypes.c_uint8),
		('server_list', AC_ACCEPT_LOGIN_SUB * 0)
    ]

# packet 0x6a
class AC_REFUSE_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8),
		('blockDate', ctypes.c_char * 20)
	]

class HC_ACCEPT_ENTER_NEO_UNION_SUB(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('money', ctypes.c_uint32),
		('jobexp', ctypes.c_uint32),
		('joblevel', ctypes.c_uint32),
		('bodystate', ctypes.c_uint32),
		('healthstate', ctypes.c_uint32),
		('effectstate', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('jobpoint', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxhp', ctypes.c_uint32),
		('sp', ctypes.c_uint16),
		('maxsp', ctypes.c_uint16),
		('speed', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('sppoint', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('Str', ctypes.c_uint8),
		('Agi', ctypes.c_uint8),
		('Vit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('Dex', ctypes.c_uint8),
		('Luk', ctypes.c_uint8),
		('CharNum', ctypes.c_uint8),
		('haircolor', ctypes.c_uint8),
		('bIsChangedCharName', ctypes.c_uint16),
		('lastMap', ctypes.c_char * 16),
		('DeleteDate', ctypes.c_uint32),
		('Robe', ctypes.c_uint32),
		('SlotAddon', ctypes.c_uint32),
		('RenameAddon', ctypes.c_uint32),
    ]
	
# packet 0x6b
class HC_ACCEPT_ENTER_NEO_UNION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('TotalSlotNum', ctypes.c_uint8),
		('PremiumStartSlot', ctypes.c_uint8),
		('PremiumEndSlot', ctypes.c_uint8),
		('dummy1_beginbilling', ctypes.c_uint8),
		('code', ctypes.c_uint32),
		('time1', ctypes.c_uint32),
		('time2', ctypes.c_uint32),
		('dummy2_endbilling', ctypes.c_char * 7),
        ('character_list', HC_ACCEPT_ENTER_NEO_UNION_SUB * 0)
    ]


# packet 0x6c
class HC_REFUSE_ENTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8)
	]


# packet 0x6d
class HC_ACCEPT_MAKECHAR_NEO_UNION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('money', ctypes.c_uint32),
		('jobexp', ctypes.c_uint32),
		('joblevel', ctypes.c_uint32),
		('bodystate', ctypes.c_uint32),
		('healthstate', ctypes.c_uint32),
		('effectstate', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('jobpoint', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxhp', ctypes.c_uint32),
		('sp', ctypes.c_uint16),
		('maxsp', ctypes.c_uint16),
		('speed', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('sppoint', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('Str', ctypes.c_uint8),
		('Agi', ctypes.c_uint8),
		('Vit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('Dex', ctypes.c_uint8),
		('Luk', ctypes.c_uint8),
		('CharNum', ctypes.c_uint8),
		('haircolor', ctypes.c_uint8),
		('bIsChangedCharName', ctypes.c_uint16)
	]


# packet 0x6e
class HC_REFUSE_MAKECHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8)
	]


# packet 0x6f
class HC_ACCEPT_DELETECHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		
    ]


# packet 0x70
class HC_REFUSE_DELETECHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8)
	]


# packet 0x71
class HC_NOTIFY_ZONESVR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('mapName', ctypes.c_char * 16),
		('ip', ctypes.c_uint32),
		('port', ctypes.c_uint16)
	]


# packet 0x72
class CZ_ENTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('AuthCode', ctypes.c_uint32),
		('clientTime', ctypes.c_uint32),
		('Sex', ctypes.c_uint8)
	]


# packet 0x73
class ZC_ACCEPT_ENTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('startTime', ctypes.c_uint32),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8)
	]


# packet 0x74
class ZC_REFUSE_ENTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8)
	]


# packet 0x75
class ZC_NOTIFY_INITCHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Style', ctypes.c_uint16),
		('Item', ctypes.c_uint8)
	]


# packet 0x76
class ZC_NOTIFY_UPDATECHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Style', ctypes.c_uint16),
		('Item', ctypes.c_uint8)
	]


# packet 0x77
class ZC_NOTIFY_UPDATEPLAYER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Style', ctypes.c_uint16),
		('Item', ctypes.c_uint8)
	]


# packet 0x78
class ZC_NOTIFY_STANDENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x79
class ZC_NOTIFY_NEWENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x7a
class ZC_NOTIFY_ACTENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('action', ctypes.c_uint8),
		('actStartTime', ctypes.c_uint32),
		('clevel', ctypes.c_uint16)
	]


# packet 0x7b
class ZC_NOTIFY_MOVEENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x7c
class ZC_NOTIFY_STANDENTRY_NPC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8)
	]


# packet 0x7d
class CZ_NOTIFY_ACTORINIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x7e
class CZ_REQUEST_TIME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('clientTime', ctypes.c_uint32)
	]


# packet 0x7f
class ZC_NOTIFY_TIME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('time', ctypes.c_uint32)
	]


# packet 0x80
class ZC_NOTIFY_VANISH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('type', ctypes.c_uint8)
	]


# packet 0x81
class SC_NOTIFY_BAN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8)
	]


# packet 0x82
class CZ_REQUEST_QUIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x83
class ZC_ACCEPT_QUIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x84
class ZC_REFUSE_QUIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x85
class CZ_REQUEST_MOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dest', ctypes.c_char * 3)
	]


# packet 0x86
class ZC_NOTIFY_MOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('MoveData', ctypes.c_char * 6),
		('moveStartTime', ctypes.c_uint32)
	]


# packet 0x87
class ZC_NOTIFY_PLAYERMOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('MoveData', ctypes.c_char * 6)
	]


# packet 0x88
class ZC_STOPMOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x89
class CZ_REQUEST_ACT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('targetGID', ctypes.c_uint32),
		('action', ctypes.c_uint8)
	]


# packet 0x8a
class ZC_NOTIFY_ACT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('targetGID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('attackMT', ctypes.c_uint32),
		('attackedMT', ctypes.c_uint32),
		('damage', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8),
		('leftDamage', ctypes.c_uint16)
	]


# packet 0x8b
class ZC_NOTIFY_ACT_POSITION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('targetGID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('damage', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8)
	]


# packet 0x8c
class CZ_REQUEST_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
	]


# packet 0x8d
class ZC_NOTIFY_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x8e
class ZC_NOTIFY_PLAYERCHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x8f
class SERVER_ENTRY_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Header', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x90
class CZ_CONTACTNPC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('type', ctypes.c_uint8)
	]


# packet 0x91
class ZC_NPCACK_MAPMOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('mapName', ctypes.c_char * 16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x92
class ZC_NPCACK_SERVERMOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('mapName', ctypes.c_char * 16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('ip', ctypes.c_uint32),
		('port', ctypes.c_uint16)
	]


# packet 0x93
class ZC_NPCACK_ENABLE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
    ]


# packet 0x94
class CZ_REQNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x95
class ZC_ACK_REQNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('CName', ctypes.c_char * 24)
	]


# packet 0x96
class CZ_WHISPER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('receiver', ctypes.c_char * 24),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x97
class ZC_WHISPER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('sender', ctypes.c_char * 24),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x98
class ZC_ACK_WHISPER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x99
class CZ_BROADCAST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x9a
class ZC_BROADCAST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x9b
class CZ_CHANGE_DIRECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('dir', ctypes.c_uint8)
	]


# packet 0x9c
class ZC_CHANGE_DIRECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('headDir', ctypes.c_uint16),
		('dir', ctypes.c_uint8)
	]


# packet 0x9d
class ZC_ITEM_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('subX', ctypes.c_uint8),
		('subY', ctypes.c_uint8)
	]


# packet 0x9e
class ZC_ITEM_FALL_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('subX', ctypes.c_uint8),
		('subY', ctypes.c_uint8),
		('count', ctypes.c_uint16)
	]


# packet 0x9f
class CZ_ITEM_PICKUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32)
	]


# packet 0xa0
class ZC_ITEM_PICKUP_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('location', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8)
	]


# packet 0xa1
class ZC_ITEM_DISAPPEAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32)
	]


# packet 0xa2
class CZ_ITEM_THROW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


class ZC_NORMAL_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
    ]

# packet 0xa3
class ZC_NORMAL_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_NORMAL_ITEMLIST_SUB * 0)
    ]

class ZC_EQUIPMENT_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
    ]

# packet 0xa4
class ZC_EQUIPMENT_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_EQUIPMENT_ITEMLIST_SUB * 0)
    ]

class ZC_STORE_NORMAL_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
    ]

# packet 0xa5
class ZC_STORE_NORMAL_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_STORE_NORMAL_ITEMLIST_SUB * 0)
    ]


class ZC_STORE_EQUIPMENT_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]

# packet 0xa6
class ZC_STORE_EQUIPMENT_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_STORE_EQUIPMENT_ITEMLIST_SUB * 0)
    ]


# packet 0xa7
class CZ_USE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0xa8
class ZC_USE_ITEM_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xa9
class CZ_REQ_WEAR_EQUIP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint16)
	]


# packet 0xaa
class ZC_REQ_WEAR_EQUIP_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xab
class CZ_REQ_TAKEOFF_EQUIP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16)
	]


# packet 0xac
class ZC_REQ_TAKEOFF_EQUIP_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xaf
class ZC_ITEM_THROW_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0xb0
class ZC_PAR_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('varID', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0xb1
class ZC_LONGPAR_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('varID', ctypes.c_uint16),
		('amount', ctypes.c_uint32)
	]


# packet 0xb2
class CZ_RESTART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8)
	]


# packet 0xb3
class ZC_RESTART_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8)
	]


# packet 0xb4
class ZC_SAY_DIALOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0xb5
class ZC_WAIT_DIALOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0xb6
class ZC_CLOSE_DIALOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0xb7
class ZC_MENU_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0xb8
class CZ_CHOOSE_MENU(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('num', ctypes.c_uint8)
	]


# packet 0xb9
class CZ_REQ_NEXT_SCRIPT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0xba
class CZ_REQ_STATUS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

# packet 0xbb
class CZ_STATUS_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('statusID', ctypes.c_uint16),
		('changeAmount', ctypes.c_uint8)
	]


# packet 0xbc
class ZC_STATUS_CHANGE_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('statusID', ctypes.c_uint16),
		('result', ctypes.c_uint8),
		('value', ctypes.c_uint8)
	]


# packet 0xbd
class ZC_STATUS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('point', ctypes.c_uint16),
		('str', ctypes.c_uint8),
		('standardStr', ctypes.c_uint8),
		('agi', ctypes.c_uint8),
		('standardAgi', ctypes.c_uint8),
		('vit', ctypes.c_uint8),
		('standardVit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('standardInt', ctypes.c_uint8),
		('dex', ctypes.c_uint8),
		('standardDex', ctypes.c_uint8),
		('luk', ctypes.c_uint8),
		('standardLuk', ctypes.c_uint8),
		('attPower', ctypes.c_uint16),
		('refiningPower', ctypes.c_uint16),
		('max_mattPower', ctypes.c_uint16),
		('min_mattPower', ctypes.c_uint16),
		('itemdefPower', ctypes.c_uint16),
		('plusdefPower', ctypes.c_uint16),
		('mdefPower', ctypes.c_uint16),
		('plusmdefPower', ctypes.c_uint16),
		('hitSuccessValue', ctypes.c_uint16),
		('avoidSuccessValue', ctypes.c_uint16),
		('plusAvoidSuccessValue', ctypes.c_uint16),
		('criticalSuccessValue', ctypes.c_uint16),
		('ASPD', ctypes.c_uint16),
		('plusASPD', ctypes.c_uint16)
	]


# packet 0xbe
class ZC_STATUS_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('statusID', ctypes.c_uint16),
		('value', ctypes.c_uint8)
	]


# packet 0xbf
class CZ_REQ_EMOTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8)
	]


# packet 0xc0
class ZC_EMOTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('type', ctypes.c_uint8)
	]


# packet 0xc1
class CZ_REQ_USER_COUNT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

# packet 0xc2
class ZC_USER_COUNT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0xc3
class ZC_SPRITE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('value', ctypes.c_uint8)
	]


# packet 0xc4
class ZC_SELECT_DEALTYPE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0xc5
class CZ_ACK_SELECT_DEALTYPE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('type', ctypes.c_uint8)
	]


class ZC_PC_PURCHASE_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('price', ctypes.c_uint32),
		('discountprice', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
    ]
# packet 0xc6
class ZC_PC_PURCHASE_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('itemInfo', ZC_PC_PURCHASE_ITEMLIST_SUB * 0)
    ]


class ZC_PC_SELL_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('price', ctypes.c_uint32),
		('overchargeprice', ctypes.c_uint32),
    ]

# packet 0xc7
class ZC_PC_SELL_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_PC_SELL_ITEMLIST_SUB * 0)
    ]

class CZ_PC_PURCHASE_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
    ]
# packet 0xc8
class CZ_PC_PURCHASE_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', CZ_PC_PURCHASE_ITEMLIST_SUB * 0)
    ]

class CZ_PC_SELL_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16)
    ]

# packet 0xc9
class CZ_PC_SELL_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', CZ_PC_SELL_ITEMLIST_SUB * 0)
    ]


# packet 0xca
class ZC_PC_PURCHASE_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xcb
class ZC_PC_SELL_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xcc
class CZ_DISCONNECT_CHARACTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0xcd
class ZC_ACK_DISCONNECT_CHARACTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xce
class CZ_DISCONNECT_ALL_CHARACTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xcf
class CZ_SETTING_WHISPER_PC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('type', ctypes.c_uint8)
	]


# packet 0xd0
class CZ_SETTING_WHISPER_STATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8)
	]


# packet 0xd1
class ZC_SETTING_WHISPER_PC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8)
	]


# packet 0xd2
class ZC_SETTING_WHISPER_STATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8)
	]


# packet 0xd3
class CZ_REQ_WHISPER_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


class ZC_WHISPER_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('name', ctypes.c_char * 24)
	]
	
# packet 0xd4
class ZC_WHISPER_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('nameList', ZC_WHISPER_LIST_SUB * 0)
    ]


# packet 0xd5
class CZ_CREATE_CHATROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('size', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('passwd', ctypes.c_char * 8),
		('title', ctypes.c_char * 255)
    ]


# packet 0xd6
class ZC_ACK_CREATE_CHATROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xd7
class ZC_ROOM_NEWENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('roomID', ctypes.c_uint32),
		('maxcount', ctypes.c_uint16),
		('curcount', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('title', ctypes.c_char * 255)
    ]


# packet 0xd8
class ZC_DESTROY_ROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('roomID', ctypes.c_uint32)
	]


# packet 0xd9
class CZ_REQ_ENTER_ROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('roomID', ctypes.c_uint32),
		('passwd', ctypes.c_char * 8)
	]


# packet 0xda
class ZC_REFUSE_ENTER_ROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]

class ZC_ENTER_ROOM_MEMBERS(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
	   ('role', ctypes.c_uint32),
	   ('name', ctypes.c_char * 24)
    ]
        
# packet 0xdb
class ZC_ENTER_ROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('roomID', ctypes.c_uint32),
		('members', ZC_ENTER_ROOM_MEMBERS * 0)
    ]


# packet 0xdc
class ZC_MEMBER_NEWENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('curcount', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0xdd
class ZC_MEMBER_EXIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('curcount', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('type', ctypes.c_uint8)
	]


# packet 0xde
class CZ_CHANGE_CHATROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('size', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('passwd', ctypes.c_char * 8),
		('title', ctypes.c_char * 255)
    ]


# packet 0xdf
class ZC_CHANGE_CHATROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('roomID', ctypes.c_uint32),
		('maxcount', ctypes.c_uint16),
		('curcount', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('title', ctypes.c_char * 255)
    ]


# packet 0xe0
class CZ_REQ_ROLE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('role', ctypes.c_uint32),
		('name', ctypes.c_char * 24)
	]


# packet 0xe1
class ZC_ROLE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('role', ctypes.c_uint32),
		('name', ctypes.c_char * 24)
	]


# packet 0xe2
class CZ_REQ_EXPEL_MEMBER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0xe3
class CZ_EXIT_ROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xe4
class CZ_REQ_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0xe5
class ZC_REQ_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0xe6
class CZ_ACK_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xe7
class ZC_ACK_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xe8
class CZ_ADD_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0xe9
class ZC_ADD_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0xea
class ZC_ACK_ADD_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xeb
class CZ_CONCLUDE_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xec
class ZC_CONCLUDE_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('who', ctypes.c_uint8)
	]


# packet 0xed
class CZ_CANCEL_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xee
class ZC_CANCEL_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xef
class CZ_EXEC_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xf0
class ZC_EXEC_EXCHANGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0xf1
class ZC_EXCHANGEITEM_UNDO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xf2
class ZC_NOTIFY_STOREITEM_COUNTINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('curCount', ctypes.c_uint16),
		('maxCount', ctypes.c_uint16)
	]


# packet 0xf3
class CZ_MOVE_ITEM_FROM_BODY_TO_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0xf4
class ZC_ADD_ITEM_TO_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0xf5
class CZ_MOVE_ITEM_FROM_STORE_TO_BODY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0xf6
class ZC_DELETE_ITEM_FROM_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0xf7
class CZ_CLOSE_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xf8
class ZC_CLOSE_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xf9
class CZ_MAKE_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('groupName', ctypes.c_char * 24)
	]


# packet 0xfa
class ZC_ACK_MAKE_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]

class ZC_GROUP_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('AID', ctypes.c_uint32),
		('characterName', ctypes.c_char * 24),
		('mapName', ctypes.c_char * 16),
		('role', ctypes.c_uint8),
		('state', ctypes.c_uint8)
    ]

# packet 0xfb
class ZC_GROUP_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('groupName', ctypes.c_char * 24),
        ('groupList', ZC_GROUP_LIST_SUB * 0)
    ]


# packet 0xfc
class CZ_REQ_JOIN_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0xfd
class ZC_ACK_REQ_JOIN_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24),
		('answer', ctypes.c_uint8)
	]


# packet 0xfe
class ZC_REQ_JOIN_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GRID', ctypes.c_uint32),
		('groupName', ctypes.c_char * 24)
	]


# packet 0xff
class CZ_JOIN_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GRID', ctypes.c_uint32),
		('answer', ctypes.c_uint32)
	]


# packet 0x100
class CZ_REQ_LEAVE_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
    ]


# packet 0x101
class ZC_GROUPINFO_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('expOption', ctypes.c_uint32)
	]


# packet 0x102
class CZ_CHANGE_GROUPEXPOPTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('expOption', ctypes.c_uint32)
	]


# packet 0x103
class CZ_REQ_EXPEL_GROUP_MEMBER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('characterName', ctypes.c_char * 24)
	]


# packet 0x104
class ZC_ADD_MEMBER_TO_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Role', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('state', ctypes.c_uint8),
		('groupName', ctypes.c_char * 24),
		('characterName', ctypes.c_char * 24),
		('mapName', ctypes.c_char * 16)
	]


# packet 0x105
class ZC_DELETE_MEMBER_FROM_GROUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('characterName', ctypes.c_char * 24),
		('result', ctypes.c_uint8)
	]


# packet 0x106
class ZC_NOTIFY_HP_TO_GROUPM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('hp', ctypes.c_uint16),
		('maxhp', ctypes.c_uint16)
	]


# packet 0x107
class ZC_NOTIFY_POSITION_TO_GROUPM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x108
class CZ_REQUEST_CHAT_PARTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x109
class ZC_NOTIFY_CHAT_PARTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x10a
class ZC_MVP_GETTING_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16)
	]


# packet 0x10b
class ZC_MVP_GETTING_SPECIAL_EXP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('exp', ctypes.c_uint32)
	]


# packet 0x10c
class ZC_MVP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x10d
class ZC_THROW_MVPITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x10e
class ZC_SKILLINFO_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('upgradable', ctypes.c_uint8)
	]

class ZC_SKILLINFO_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('SKID', ctypes.c_uint16),
		('type', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('skillName', ctypes.c_char * 24),
		('upgradable', ctypes.c_uint8),
    ]

# packet 0x10f
class ZC_SKILLINFO_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('skillList', ZC_SKILLINFO_LIST_SUB * 1)
    ]

# packet 0x110
class ZC_ACK_TOUSESKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('NUM', ctypes.c_uint32),
		('result', ctypes.c_uint8),
		('cause', ctypes.c_uint8)
	]


# packet 0x111
class ZC_ADD_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('type', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('skillName', ctypes.c_char * 24),
		('upgradable', ctypes.c_uint8)
	]


# packet 0x112
class CZ_UPGRADE_SKILLLEVEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16)
	]


# packet 0x113
class CZ_USE_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('targetID', ctypes.c_uint32)
	]


# packet 0x114
class ZC_NOTIFY_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('targetID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('attackMT', ctypes.c_uint32),
		('attackedMT', ctypes.c_uint32),
		('damage', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8)
	]


# packet 0x115
class ZC_NOTIFY_SKILL_POSITION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('targetID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('attackMT', ctypes.c_uint32),
		('attackedMT', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('damage', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8)
	]


# packet 0x116
class CZ_USE_SKILL_TOGROUND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x117
class ZC_NOTIFY_GROUNDSKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('startTime', ctypes.c_uint32)
	]


# packet 0x118
class CZ_CANCEL_LOCKON(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x119
class ZC_STATE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8)
	]


# packet 0x11a
class ZC_USE_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('targetAID', ctypes.c_uint32),
		('srcAID', ctypes.c_uint32),
		('result', ctypes.c_uint8)
	]


# packet 0x11b
class CZ_SELECT_WARPPOINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('mapName', ctypes.c_char * 16)
	]


# packet 0x11c
class ZC_WARPLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('mapName', ctypes.c_char * 16)
	]


# packet 0x11d
class CZ_REMEMBER_WARPPOINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x11e
class ZC_ACK_REMEMBER_WARPPOINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint8)
	]


# packet 0x11f
class ZC_SKILL_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('creatorAID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('job', ctypes.c_uint8),
		('isVisible', ctypes.c_uint8)
	]


# packet 0x120
class ZC_SKILL_DISAPPEAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x121
class ZC_NOTIFY_CARTITEM_COUNTINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('curCount', ctypes.c_uint16),
		('maxCount', ctypes.c_uint16),
		('curWeight', ctypes.c_uint32),
		('maxWeight', ctypes.c_uint32)
	]

class ZC_CART_EQUIPMENT_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]
# packet 0x122
class ZC_CART_EQUIPMENT_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_CART_EQUIPMENT_ITEMLIST_SUB * 0)
    ]


class ZC_CART_NORMAL_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16)
    ]

# packet 0x123
class ZC_CART_NORMAL_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('itemInfo', ZC_CART_NORMAL_ITEMLIST_SUB * 0)
    ]


# packet 0x124
class ZC_ADD_ITEM_TO_CART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0x125
class ZC_DELETE_ITEM_FROM_CART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x126
class CZ_MOVE_ITEM_FROM_BODY_TO_CART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x127
class CZ_MOVE_ITEM_FROM_CART_TO_BODY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x128
class CZ_MOVE_ITEM_FROM_STORE_TO_CART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x129
class CZ_MOVE_ITEM_FROM_CART_TO_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x12a
class CZ_REQ_CARTOFF(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
	]


# packet 0x12b
class ZC_CARTOFF(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x12c
class ZC_ACK_ADDITEM_TO_CART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x12d
class ZC_OPENSTORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('itemcount', ctypes.c_uint16)
	]


# packet 0x12e
class CZ_REQ_CLOSESTORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class CZ_REQ_OPENSTORE_SUB(ctypes.Structure):
    _pack_ = 1 
    _fields_ = [
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('Price', ctypes.c_uint32),
    ]

# packet 0x12f
class CZ_REQ_OPENSTORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('storeName', ctypes.c_char * 80),
        ('itemInfo', CZ_REQ_OPENSTORE_SUB * 0)
    ]


# packet 0x130
class CZ_REQ_BUY_FROMMC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x131
class ZC_STORE_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32),
		('storeName', ctypes.c_char * 80)
	]


# packet 0x132
class ZC_DISAPPEAR_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32)
	]

class ZC_PC_PURCHASE_ITEMLIST_FROMMC_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('price', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]
# packet 0x133
class ZC_PC_PURCHASE_ITEMLIST_FROMMC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
        ('itemInfo', ZC_PC_PURCHASE_ITEMLIST_FROMMC_SUB * 0)
    ]


class CZ_PC_PURCHASE_ITEMLIST_FROMMC_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('count', ctypes.c_uint16),
		('index', ctypes.c_uint16),
    ]

# packet 0x134
class CZ_PC_PURCHASE_ITEMLIST_FROMMC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
        ('itemInfo', CZ_PC_PURCHASE_ITEMLIST_FROMMC_SUB * 0)
    ]


# packet 0x135
class ZC_PC_PURCHASE_RESULT_FROMMC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('curcount', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]

class ZC_PC_PURCHASE_MYITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
   		('price', ctypes.c_uint32),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]

# packet 0x136
class ZC_PC_PURCHASE_MYITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
        ('itemInfo', ZC_PC_PURCHASE_MYITEMLIST_SUB * 0)
    ]


# packet 0x137
class ZC_DELETEITEM_FROM_MCSTORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0x138
class CZ_PKMODE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('isTurnOn', ctypes.c_uint8)
	]


# packet 0x139
class ZC_ATTACK_FAILURE_FOR_DISTANCE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('targetAID', ctypes.c_uint32),
		('targetXPos', ctypes.c_uint16),
		('targetYPos', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('currentAttRange', ctypes.c_uint16)
	]


# packet 0x13a
class ZC_ATTACK_RANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('currentAttRange', ctypes.c_uint16)
	]


# packet 0x13b
class ZC_ACTION_FAILURE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x13c
class ZC_EQUIP_ARROW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16)
	]


# packet 0x13d
class ZC_RECOVERY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('varID', ctypes.c_uint16),
		('amount', ctypes.c_uint16)
	]


# packet 0x13e
class ZC_USESKILL_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('targetID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('property', ctypes.c_uint32),
		('delayTime', ctypes.c_uint32)
	]


# packet 0x13f
class CZ_ITEM_CREATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('itemName', ctypes.c_char * 24)
	]


# packet 0x140
class CZ_MOVETO_MAP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('mapName', ctypes.c_char * 16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x141
class ZC_COUPLESTATUS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('statusType', ctypes.c_uint32),
		('defaultStatus', ctypes.c_uint32),
		('plusStatus', ctypes.c_uint32)
	]


# packet 0x142
class ZC_OPEN_EDITDLG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0x143
class CZ_INPUT_EDITDLG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('value', ctypes.c_uint32)
	]


# packet 0x144
class ZC_COMPASS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('type', ctypes.c_uint32),
		('xPos', ctypes.c_uint32),
		('yPos', ctypes.c_uint32),
		('id', ctypes.c_uint8),
		('color', ctypes.c_uint32)
	]


# packet 0x145
class ZC_SHOW_IMAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('imageName', ctypes.c_char * 16),
		('type', ctypes.c_uint8)
	]


# packet 0x146
class CZ_CLOSE_DIALOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0x147
class ZC_AUTORUN_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('type', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('skillName', ctypes.c_char * 24),
		('upgradable', ctypes.c_uint8)
	]


# packet 0x148
class ZC_RESURRECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('type', ctypes.c_uint16)
	]


# packet 0x149
class CZ_REQ_GIVE_MANNER_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('otherAID', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('point', ctypes.c_uint16)
	]


# packet 0x14a
class ZC_ACK_GIVE_MANNER_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint32)
	]


# packet 0x14b
class ZC_NOTIFY_MANNER_POINT_GIVEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('otherCharName', ctypes.c_char * 24)
	]

class ZC_MYGUILD_BASIC_INFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('GDID', ctypes.c_uint32),
		('relation', ctypes.c_uint32),
		('GuildName', ctypes.c_char * 24),
    ]
# packet 0x14c
class ZC_MYGUILD_BASIC_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('info', ZC_MYGUILD_BASIC_INFO_SUB * 1)
    ]

# packet 0x14d
class CZ_REQ_GUILD_MENUINTERFACE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x14e
class ZC_ACK_GUILD_MENUINTERFACE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('guildMemuFlag', ctypes.c_uint32)
	]


# packet 0x14f
class CZ_REQ_GUILD_MENU(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint32)
	]


# packet 0x150
class ZC_GUILD_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('level', ctypes.c_uint32),
		('userNum', ctypes.c_uint32),
		('maxUserNum', ctypes.c_uint32),
		('userAverageLevel', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('maxExp', ctypes.c_uint32),
		('point', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('emblemVersion', ctypes.c_uint32),
		('guildname', ctypes.c_char * 24),
		('masterName', ctypes.c_char * 24),
		('manageLand', ctypes.c_char * 16)
	]


# packet 0x151
class CZ_REQ_GUILD_EMBLEM_IMG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32)
	]


# packet 0x152
class ZC_GUILD_EMBLEM_IMG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('emblemVersion', ctypes.c_uint32),
		('img', ctypes.c_char * 255)
    ]


# packet 0x153
class CZ_REGISTER_GUILD_EMBLEM_IMG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('img', ctypes.c_char * 255)
    ]


class ZC_MEMBER_INFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('HeadType', ctypes.c_uint16),
		('HeadPalette', ctypes.c_uint16),
		('Sex', ctypes.c_uint16),
		('Job', ctypes.c_uint16),
		('Level', ctypes.c_uint16),
		('MemberExp', ctypes.c_uint32),
		('CurrentState', ctypes.c_uint32),
		('GPositionID', ctypes.c_uint32),
		('Memo', ctypes.c_char * 50),
		('CharName', ctypes.c_char * 24),
    ]

# packet 0x154
class ZC_MEMBERMGR_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('memberInfo', ZC_MEMBER_INFO_SUB * 1)
    ]

class CZ_REQ_CHANGE_MEMBERPOS_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('positionID', ctypes.c_uint32),
    ]
# packet 0x155
class CZ_REQ_CHANGE_MEMBERPOS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('memberInfo', CZ_REQ_CHANGE_MEMBERPOS_SUB * 1)
    ]

class ZC_ACK_REQ_CHANGE_MEMBERS_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('positionID', ctypes.c_uint32),
    ]
# packet 0x156
class ZC_ACK_REQ_CHANGE_MEMBERS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('memberInfo', ZC_ACK_REQ_CHANGE_MEMBERS_SUB * 1)
    ]


# packet 0x157
class CZ_REQ_OPEN_MEMBER_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x158
class ZC_ACK_OPEN_MEMBER_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x159
class CZ_REQ_LEAVE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('reasonDesc', ctypes.c_char * 40)
	]


# packet 0x15a
class ZC_ACK_LEAVE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('charName', ctypes.c_char * 24),
		('reasonDesc', ctypes.c_char * 40)
	]


# packet 0x15b
class CZ_REQ_BAN_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('reasonDesc', ctypes.c_char * 40)
	]


# packet 0x15c
class ZC_ACK_BAN_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('charName', ctypes.c_char * 24),
		('reasonDesc', ctypes.c_char * 40),
		('account', ctypes.c_char * 24)
	]


# packet 0x15d
class CZ_REQ_DISORGANIZE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('key', ctypes.c_char * 40)
	]


# packet 0x15e
class ZC_ACK_DISORGANIZE_GUILD_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('reason', ctypes.c_uint32)
	]


# packet 0x15f
class ZC_ACK_DISORGANIZE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('reasonDesc', ctypes.c_char * 40)
	]

class ZC_POSITION_INFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('positionID', ctypes.c_uint32),
		('right', ctypes.c_uint32),
		('ranking', ctypes.c_uint32),
		('payRate', ctypes.c_uint32),
    ]
# packet 0x160
class ZC_POSITION_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('positionInfo', ZC_POSITION_INFO_SUB * 1)
    ]

class CZ_REG_CHANGE_GUILD_POSITIONINFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('positionID', ctypes.c_uint32),
		('right', ctypes.c_uint32),
		('ranking', ctypes.c_uint32),
		('payRate', ctypes.c_uint32),
		('posName', ctypes.c_char * 24),
    ]

# packet 0x161
class CZ_REG_CHANGE_GUILD_POSITIONINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('positionInfo', CZ_REG_CHANGE_GUILD_POSITIONINFO_SUB * 1)
    ]

class ZC_GUILD_SKILLINFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('SKID', ctypes.c_uint16),
		('type', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('skillName', ctypes.c_char * 24),
		('upgradable', ctypes.c_uint8),
    ]

# packet 0x162
class ZC_GUILD_SKILLINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('skillPoint', ctypes.c_uint16),
        ('skillInfo', ZC_GUILD_SKILLINFO_SUB * 1)
    ]

class ZC_BAN_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('charname', ctypes.c_char * 24),
		('account', ctypes.c_char * 24),
		('reason', ctypes.c_char * 40),
    ]

# packet 0x163
class ZC_BAN_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('banList', ZC_BAN_LIST_SUB * 1)
    ]

class ZC_OTHER_GUILD_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('guildname', ctypes.c_char * 24),
		('guildLevel', ctypes.c_uint32),
		('guildMemberSize', ctypes.c_uint32),
		('guildRanking', ctypes.c_uint32)
    ]

# packet 0x164
class ZC_OTHER_GUILD_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('guildList', ZC_OTHER_GUILD_LIST_SUB * 1)
    ]


# packet 0x165
class CZ_REQ_MAKE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('GName', ctypes.c_char * 24)
	]

class ZC_POSITION_ID_NAME_INFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('positionID', ctypes.c_uint32),
		('posName', ctypes.c_char * 24)
    ]

# packet 0x166
class ZC_POSITION_ID_NAME_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('positionInfo', ZC_POSITION_ID_NAME_INFO_SUB * 1)
    ]


# packet 0x167
class ZC_RESULT_MAKE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x168
class CZ_REQ_JOIN_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('MyAID', ctypes.c_uint32),
		('MyGID', ctypes.c_uint32)
	]


# packet 0x169
class ZC_ACK_REQ_JOIN_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('answer', ctypes.c_uint8)
	]


# packet 0x16a
class ZC_REQ_JOIN_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('guildName', ctypes.c_char * 24)
	]


# packet 0x16b
class CZ_JOIN_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('answer', ctypes.c_uint32)
	]


# packet 0x16c
class ZC_UPDATE_GDID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('emblemVersion', ctypes.c_uint32),
		('right', ctypes.c_uint32),
		('isMaster', ctypes.c_uint8),
		('InterSID', ctypes.c_uint32),
		('GName', ctypes.c_char * 24)
	]


# packet 0x16d
class ZC_UPDATE_CHARSTAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('status', ctypes.c_uint32)
	]


# packet 0x16e
class CZ_GUILD_NOTICE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('subject', ctypes.c_char * 60),
		('notice', ctypes.c_char * 120)
	]


# packet 0x16f
class ZC_GUILD_NOTICE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('subject', ctypes.c_char * 60),
		('notice', ctypes.c_char * 120)
	]


# packet 0x170
class CZ_REQ_ALLY_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('MyAID', ctypes.c_uint32),
		('MyGID', ctypes.c_uint32)
	]


# packet 0x171
class ZC_REQ_ALLY_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('otherAID', ctypes.c_uint32),
		('guildName', ctypes.c_char * 24)
	]


# packet 0x172
class CZ_ALLY_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('otherAID', ctypes.c_uint32),
		('answer', ctypes.c_uint32)
	]


# packet 0x173
class ZC_ACK_REQ_ALLY_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('answer', ctypes.c_uint8)
	]

class ZC_ACK_CHANGE_GUILD_POSITIONINFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('positionID', ctypes.c_uint32),
		('right', ctypes.c_uint32),
		('ranking', ctypes.c_uint32),
		('payRate', ctypes.c_uint32),
		('posName', ctypes.c_char * 24)
    ]

# packet 0x174
class ZC_ACK_CHANGE_GUILD_POSITIONINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('positionInfo', ZC_ACK_CHANGE_GUILD_POSITIONINFO_SUB * 0)
    ]


# packet 0x175
class CZ_REQ_GUILD_MEMBER_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x176
class ZC_ACK_GUILD_MEMBER_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('head', ctypes.c_uint16),
		('headPalette', ctypes.c_uint16),
		('sex', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('contributionExp', ctypes.c_uint32),
		('currentState', ctypes.c_uint32),
		('positionID', ctypes.c_uint32),
		('intro', ctypes.c_char * 50),
		('charname', ctypes.c_char * 24)
	]


# packet 0x177
class ZC_ITEMIDENTIFY_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ITIDList', ctypes.c_uint16)
	]


# packet 0x178
class CZ_REQ_ITEMIDENTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16)
	]


# packet 0x179
class ZC_ACK_ITEMIDENTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x17a
class CZ_REQ_ITEMCOMPOSITION_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('cardIndex', ctypes.c_uint16)
	]


# packet 0x17b
class ZC_ITEMCOMPOSITION_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ITIDList', ctypes.c_uint16)
	]


# packet 0x17c
class CZ_REQ_ITEMCOMPOSITION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('cardIndex', ctypes.c_uint16),
		('equipIndex', ctypes.c_uint16)
	]


# packet 0x17d
class ZC_ACK_ITEMCOMPOSITION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('equipIndex', ctypes.c_uint16),
		('cardIndex', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x17e
class CZ_GUILD_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x17f
class ZC_GUILD_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x180
class CZ_REQ_HOSTILE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x181
class ZC_ACK_REQ_HOSTILE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x182
class ZC_MEMBER_ADD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('head', ctypes.c_uint16),
		('headPalette', ctypes.c_uint16),
		('sex', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('contributionExp', ctypes.c_uint32),
		('currentState', ctypes.c_uint32),
		('positionID', ctypes.c_uint32),
		('intro', ctypes.c_char * 50),
		('charname', ctypes.c_char * 24)
	]


# packet 0x183
class CZ_REQ_DELETE_RELATED_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('OpponentGDID', ctypes.c_uint32),
		('Relation', ctypes.c_uint32)
	]


# packet 0x184
class ZC_DELETE_RELATED_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('OpponentGDID', ctypes.c_uint32),
		('Relation', ctypes.c_uint32)
	]


# packet 0x185
class ZC_ADD_RELATED_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('relation', ctypes.c_uint32),
		('GDID', ctypes.c_uint32),
		('guildname', ctypes.c_char * 24)
	]


# packet 0x186
class COLLECTORDEAD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ServerID', ctypes.c_uint32)
	]


# packet 0x187
class PING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x188
class ZC_ACK_ITEMREFINING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint16),
		('itemIndex', ctypes.c_uint16),
		('refiningLevel', ctypes.c_uint16)
	]


# packet 0x189
class ZC_NOTIFY_MAPINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x18a
class CZ_REQ_DISCONNECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x18b
class ZC_ACK_REQ_DISCONNECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint16)
	]


# packet 0x18c
class ZC_MONSTER_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('size', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('_def', ctypes.c_uint16),
		('raceType', ctypes.c_uint16),
		('mdefPower', ctypes.c_uint16),
		('property', ctypes.c_uint16),
		('water', ctypes.c_uint8),
		('earth', ctypes.c_uint8),
		('fire', ctypes.c_uint8),
		('wind', ctypes.c_uint8),
		('poison', ctypes.c_uint8),
		('saint', ctypes.c_uint8),
		('dark', ctypes.c_uint8),
		('mental', ctypes.c_uint8),
		('undead', ctypes.c_uint8)
	]


# packet 0x18d
class ZC_MAKABLEITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('material_ID', ctypes.c_uint16)
	]


# packet 0x18e
class CZ_REQMAKINGITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('material_ID', ctypes.c_uint16)
	]


# packet 0x18f
class ZC_ACK_REQMAKINGITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint16),
		('ITID', ctypes.c_uint16)
	]


# packet 0x190
class CZ_USE_SKILL_TOGROUND_WITHTALKBOX(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('contents', ctypes.c_char * 80)
	]


# packet 0x191
class ZC_TALKBOX_CHATCONTENTS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('contents', ctypes.c_char * 80)
	]


# packet 0x192
class ZC_UPDATE_MAPINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('type', ctypes.c_uint16),
		('mapName', ctypes.c_char * 16)
	]


# packet 0x193
class CZ_REQNAME_BYGID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x194
class ZC_ACK_REQNAME_BYGID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('CName', ctypes.c_char * 24)
	]


# packet 0x195
class ZC_ACK_REQNAMEALL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('CName', ctypes.c_char * 24),
		('PName', ctypes.c_char * 24),
		('GName', ctypes.c_char * 24),
		('RName', ctypes.c_char * 24)
	]


# packet 0x196
class ZC_MSG_STATE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('state', ctypes.c_uint8)
	]


# packet 0x197
class CZ_RESET(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x198
class CZ_CHANGE_MAPTYPE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x199
class ZC_NOTIFY_MAPPROPERTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x19a
class ZC_NOTIFY_RANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('ranking', ctypes.c_uint32),
		('total', ctypes.c_uint32)
	]


# packet 0x19b
class ZC_NOTIFY_EFFECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('effectID', ctypes.c_uint32)
	]


# packet 0x19d
class CZ_CHANGE_EFFECTSTATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EffectState', ctypes.c_uint32)
	]


# packet 0x19e
class ZC_START_CAPTURE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x19f
class CZ_TRYCAPTURE_MONSTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('targetAID', ctypes.c_uint32)
	]


# packet 0x1a0
class ZC_TRYCAPTURE_MONSTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x1a1
class CZ_COMMAND_PET(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('cSub', ctypes.c_uint8)
	]


# packet 0x1a2
class ZC_PROPERTY_PET(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('szName', ctypes.c_char * 24),
		('bModified', ctypes.c_uint8),
		('nLevel', ctypes.c_uint16),
		('nFullness', ctypes.c_uint16),
		('nRelationship', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('job', ctypes.c_uint16)
	]


# packet 0x1a3
class ZC_FEED_PET(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('cRet', ctypes.c_uint8),
		('ITID', ctypes.c_uint16)
	]


# packet 0x1a4
class ZC_CHANGESTATE_PET(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('data', ctypes.c_uint32)
	]


# packet 0x1a5
class CZ_RENAME_PET(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('szName', ctypes.c_char * 24)
	]

class ZC_PETEGG_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16)
    ]
# packet 0x1a6
class ZC_PETEGG_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('list', ZC_PETEGG_LIST_SUB * 0)
    ]

# packet 0x1a7
class CZ_SELECT_PETEGG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16)
	]


# packet 0x1a8
class CZ_PETEGG_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16)
	]


# packet 0x1a9
class CZ_PET_ACT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('data', ctypes.c_uint32)
	]


# packet 0x1aa
class ZC_PET_ACT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('data', ctypes.c_uint32)
	]


# packet 0x1ab
class ZC_PAR_CHANGE_USER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('varID', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x1ac
class ZC_SKILL_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]

class ZC_MAKINGARROW_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16)
    ]

# packet 0x1ad
class ZC_MAKINGARROW_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('list', ZC_MAKINGARROW_LIST_SUB * 0)
    ]


# packet 0x1ae
class CZ_REQ_MAKINGARROW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('id', ctypes.c_uint16)
	]


# packet 0x1af
class CZ_REQ_CHANGECART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('num', ctypes.c_uint16)
	]


# packet 0x1b0
class ZC_NPCSPRITE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('value', ctypes.c_uint32)
	]


# packet 0x1b1
class ZC_SHOWDIGIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('value', ctypes.c_uint32)
	]

class CZ_REQ_OPENSTORE2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('Price', ctypes.c_uint32)
    ]
# packet 0x1b2
class CZ_REQ_OPENSTORE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('storeName', ctypes.c_char * 80),
		('result', ctypes.c_uint8),
        ('list', CZ_REQ_OPENSTORE2_SUB * 0)
    ]


# packet 0x1b3
class ZC_SHOW_IMAGE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('imageName', ctypes.c_char * 64),
		('type', ctypes.c_uint8)
	]


# packet 0x1b4
class ZC_CHANGE_GUILD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GDID', ctypes.c_uint32),
		('emblemVersion', ctypes.c_uint16)
	]


# packet 0x1b5
class SC_BILLING_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dwAmountRemain', ctypes.c_uint32),
		('dwQuantityRemain', ctypes.c_uint32),
		('dwReserved1', ctypes.c_uint32),
		('dwReserved2', ctypes.c_uint32)
	]


# packet 0x1b6
class ZC_GUILD_INFO2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('level', ctypes.c_uint32),
		('userNum', ctypes.c_uint32),
		('maxUserNum', ctypes.c_uint32),
		('userAverageLevel', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('maxExp', ctypes.c_uint32),
		('point', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('emblemVersion', ctypes.c_uint32),
		('guildname', ctypes.c_char * 24),
		('masterName', ctypes.c_char * 24),
		('manageLand', ctypes.c_char * 16),
		('zeny', ctypes.c_uint32)
	]


# packet 0x1b7
class CZ_GUILD_ZENY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('zeny', ctypes.c_uint32)
	]


# packet 0x1b8
class ZC_GUILD_ZENY_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ret', ctypes.c_uint8)
	]


# packet 0x1b9
class ZC_DISPEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x1ba
class CZ_REMOVE_AID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AccountName', ctypes.c_char * 24)
	]


# packet 0x1bb
class CZ_SHIFT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CharacterName', ctypes.c_char * 24)
	]


# packet 0x1bc
class CZ_RECALL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AccountName', ctypes.c_char * 24)
	]


# packet 0x1bd
class CZ_RECALL_GID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CharacterName', ctypes.c_char * 24)
	]


# packet 0x1be
class AC_ASK_PNGAMEROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1bf
class CA_REPLY_PNGAMEROOM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Permission', ctypes.c_uint8)
	]


# packet 0x1c0
class CZ_REQ_REMAINTIME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1c1
class ZC_REPLY_REMAINTIME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint32),
		('ExpirationDate', ctypes.c_uint32),
		('RemainTime', ctypes.c_uint32)
	]


# packet 0x1c2
class ZC_INFO_REMAINTIME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint32),
		('RemainTime', ctypes.c_uint32)
	]


# packet 0x1c3
class ZC_BROADCAST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('fontColor', ctypes.c_uint32),
		('fontType', ctypes.c_uint16),
		('fontSize', ctypes.c_uint16),
		('fontAlign', ctypes.c_uint16),
		('fontY', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x1c4
class ZC_ADD_ITEM_TO_STORE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0x1c5
class ZC_ADD_ITEM_TO_CART2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0x1c6
class CS_REQ_ENCRYPTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('encCount', ctypes.c_uint8),
		('decCount', ctypes.c_uint8)
	]


# packet 0x1c7
class SC_ACK_ENCRYPTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1c8
class ZC_USE_ITEM_ACK2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('id', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x1c9
class ZC_SKILL_ENTRY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('creatorAID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('job', ctypes.c_uint8),
		('isVisible', ctypes.c_uint8),
		('isContens', ctypes.c_uint8),
		('msg', ctypes.c_char * 80)
	]


# packet 0x1ca
class CZ_REQMAKINGHOMUN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x1cb
class CZ_MONSTER_TALK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('stateId', ctypes.c_uint8),
		('skillId', ctypes.c_uint8),
		('arg1', ctypes.c_uint8)
	]


# packet 0x1cc
class ZC_MONSTER_TALK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('stateId', ctypes.c_uint8),
		('skillId', ctypes.c_uint8),
		('arg1', ctypes.c_uint8)
	]


# packet 0x1cd
class ZC_AUTOSPELLLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint32)
	]


# packet 0x1ce
class CZ_SELECTAUTOSPELL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint32)
	]


# packet 0x1cf
class ZC_DEVOTIONLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('myAID', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('range', ctypes.c_uint16)
	]


# packet 0x1d0
class ZC_SPIRITS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('num', ctypes.c_uint16)
	]


# packet 0x1d1
class ZC_BLADESTOP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('srcAID', ctypes.c_uint32),
		('destAID', ctypes.c_uint32),
		('flag', ctypes.c_uint32)
	]


# packet 0x1d2
class ZC_COMBODELAY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('delayTime', ctypes.c_uint32)
	]


# packet 0x1d3
class ZC_SOUND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('fileName', ctypes.c_char * 24),
		('act', ctypes.c_uint8),
		('term', ctypes.c_uint32),
		('NAID', ctypes.c_uint32)
	]


# packet 0x1d4
class ZC_OPEN_EDITDLGSTR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0x1d5
class CZ_INPUT_EDITDLGSTR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x1d6
class ZC_NOTIFY_MAPPROPERTY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x1d7
class ZC_SPRITE_CHANGE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('value', ctypes.c_uint32)
	]


# packet 0x1d8
class ZC_NOTIFY_STANDENTRY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x1d9
class ZC_NOTIFY_NEWENTRY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x1da
class ZC_NOTIFY_MOVEENTRY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint16),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x1db
class CA_REQ_HASH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1dc
class AC_ACK_HASH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('secret', ctypes.c_char * 255)
    ]


# packet 0x1dd
class CA_LOGIN2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('PasswdMD5', ctypes.c_char * 16),
		('clienttype', ctypes.c_uint8)
	]


# packet 0x1de
class ZC_NOTIFY_SKILL2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('targetID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('attackMT', ctypes.c_uint32),
		('attackedMT', ctypes.c_uint32),
		('damage', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8)
	]


# packet 0x1df
class CZ_REQ_ACCOUNTNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x1e0
class ZC_ACK_ACCOUNTNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('name', ctypes.c_char * 24)
	]


# packet 0x1e1
class ZC_SPIRITS2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('num', ctypes.c_uint16)
	]


# packet 0x1e2
class ZC_REQ_COUPLE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('name', ctypes.c_char * 24)
	]


# packet 0x1e3
class CZ_JOIN_COUPLE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('answer', ctypes.c_uint32)
	]


# packet 0x1e4
class ZC_START_COUPLE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1e5
class CZ_REQ_JOIN_COUPLE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x1e6
class ZC_COUPLENAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CoupleName', ctypes.c_char * 24)
	]


# packet 0x1e7
class CZ_DORIDORI(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1e8
class CZ_MAKE_GROUP2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('groupName', ctypes.c_char * 24),
		('ItemPickupRule', ctypes.c_uint8),
		('ItemDivisionRule', ctypes.c_uint8)
	]


# packet 0x1e9
class ZC_ADD_MEMBER_TO_GROUP2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Role', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('state', ctypes.c_uint8),
		('groupName', ctypes.c_char * 24),
		('characterName', ctypes.c_char * 24),
		('mapName', ctypes.c_char * 16),
		('ItemPickupRule', ctypes.c_uint8),
		('ItemDivisionRule', ctypes.c_uint8)
	]


# packet 0x1ea
class ZC_CONGRATULATION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x1eb
class ZC_NOTIFY_POSITION_TO_GUILDM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x1ec
class ZC_GUILD_MEMBER_MAP_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GDID', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('mapName', ctypes.c_char * 16)
	]


# packet 0x1ed
class CZ_CHOPOKGI(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class ZC_NORMAL_ITEMLIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
    ]

# packet 0x1ee
class ZC_NORMAL_ITEMLIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_NORMAL_ITEMLIST2_SUB * 0)
    ]

class ZC_CART_NORMAL_ITEMLIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
    ]
# packet 0x1ef
class ZC_CART_NORMAL_ITEMLIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemInfo', ZC_CART_NORMAL_ITEMLIST2_SUB * 0)
    ]

class ZC_STORE_NORMAL_ITEMLIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
    ]

# packet 0x1f0
class ZC_STORE_NORMAL_ITEMLIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_STORE_NORMAL_ITEMLIST2_SUB * 0)
    ]


# packet 0x1f1
class AC_NOTIFY_ERROR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x1f2
class ZC_UPDATE_CHARSTAT2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('status', ctypes.c_uint32),
		('sex', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('headPalette', ctypes.c_uint16)
	]


# packet 0x1f3
class ZC_NOTIFY_EFFECT2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('effectID', ctypes.c_uint32)
	]


# packet 0x1f4
class ZC_REQ_EXCHANGE_ITEM2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('GID', ctypes.c_uint32),
		('level', ctypes.c_uint16)
	]


# packet 0x1f5
class ZC_ACK_EXCHANGE_ITEM2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('level', ctypes.c_uint16)
	]


# packet 0x1f6
class ZC_REQ_BABY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('name', ctypes.c_char * 24)
	]


# packet 0x1f7
class CZ_JOIN_BABY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('answer', ctypes.c_uint32)
	]


# packet 0x1f8
class ZC_START_BABY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x1f9
class CZ_REQ_JOIN_BABY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x1fa
class CA_LOGIN3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('PasswdMD5', ctypes.c_char * 16),
		('clienttype', ctypes.c_uint8),
		('ClientInfo', ctypes.c_uint8)
	]


# packet 0x1fb
class CH_DELETE_CHAR2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('key', ctypes.c_char * 50)
	]

class ZC_REPAIRITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
    ]

# packet 0x1fc
class ZC_REPAIRITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_REPAIRITEMLIST_SUB * 0)
    ]


# packet 0x1fd
class CZ_REQ_ITEMREPAIR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0x1fe
class ZC_ACK_ITEMREPAIR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x1ff
class ZC_HIGHJUMP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x200
class CA_CONNECT_INFO_CHANGED(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ID', ctypes.c_char * 24)
	]

class ZC_FRIENDS_LIST_SUB(ctypes.Structure):
    _pack_ = 1 
    _fields_ = [   
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('Name', ctypes.c_char * 24)
    ]
# packet 0x201
class ZC_FRIENDS_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('friendsList', ZC_FRIENDS_LIST_SUB * 0)
    ]


# packet 0x202
class CZ_ADD_FRIENDS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0x203
class CZ_DELETE_FRIENDS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32)
	]


# packet 0x204
class CA_EXE_HASHCHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('HashValue', ctypes.c_char * 16)
	]


# packet 0x205
class ZC_DIVORCE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0x206
class ZC_FRIENDS_STATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('State', ctypes.c_uint8)
	]


# packet 0x207
class ZC_REQ_ADD_FRIENDS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ReqAID', ctypes.c_uint32),
		('ReqGID', ctypes.c_uint32),
		('Name', ctypes.c_char * 24)
	]


# packet 0x208
class CZ_ACK_REQ_ADD_FRIENDS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ReqAID', ctypes.c_uint32),
		('ReqGID', ctypes.c_uint32),
		('Result', ctypes.c_uint32)
	]


# packet 0x209
class ZC_ADD_FRIENDS_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('Name', ctypes.c_char * 24)
	]


# packet 0x20a
class ZC_DELETE_FRIENDS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32)
	]


# packet 0x20b
class CH_EXE_HASHCHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ClientType', ctypes.c_uint8),
		('HashValue', ctypes.c_char * 16)
	]


# packet 0x20c
class CZ_EXE_HASHCHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ClientType', ctypes.c_uint8),
		('HashValue', ctypes.c_char * 16)
	]

class ZC_BLOCK_CHARACTER_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('GID', ctypes.c_uint32),
		('szExpireDate', ctypes.c_char * 20)
    ]
# packet 0x20d
class HC_BLOCK_CHARACTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('blockList', ZC_BLOCK_CHARACTER_SUB * 0)
    ]


# packet 0x20e
class ZC_STARSKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('mapName', ctypes.c_char * 24),
		('monsterID', ctypes.c_uint32),
		('star', ctypes.c_uint8),
		('result', ctypes.c_uint8)
	]


# packet 0x20f
class CZ_REQ_PVPPOINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32)
	]


# packet 0x210
class ZC_ACK_PVPPOINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('WinPoint', ctypes.c_uint32),
		('LosePoint', ctypes.c_uint32),
		('Point', ctypes.c_uint32)
	]


# packet 0x211
class ZH_MOVE_PVPWORLD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x212
class CZ_REQ_GIVE_MANNER_BYNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CharName', ctypes.c_char * 24)
	]


# packet 0x213
class CZ_REQ_STATUS_GM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CharName', ctypes.c_char * 24)
	]


# packet 0x214
class ZC_ACK_STATUS_GM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('str', ctypes.c_uint8),
		('standardStr', ctypes.c_uint8),
		('agi', ctypes.c_uint8),
		('standardAgi', ctypes.c_uint8),
		('vit', ctypes.c_uint8),
		('standardVit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('standardInt', ctypes.c_uint8),
		('dex', ctypes.c_uint8),
		('standardDex', ctypes.c_uint8),
		('luk', ctypes.c_uint8),
		('standardLuk', ctypes.c_uint8),
		('attPower', ctypes.c_uint16),
		('refiningPower', ctypes.c_uint16),
		('max_mattPower', ctypes.c_uint16),
		('min_mattPower', ctypes.c_uint16),
		('itemdefPower', ctypes.c_uint16),
		('plusdefPower', ctypes.c_uint16),
		('mdefPower', ctypes.c_uint16),
		('plusmdefPower', ctypes.c_uint16),
		('hitSuccessValue', ctypes.c_uint16),
		('avoidSuccessValue', ctypes.c_uint16),
		('plusAvoidSuccessValue', ctypes.c_uint16),
		('criticalSuccessValue', ctypes.c_uint16),
		('ASPD', ctypes.c_uint16),
		('plusASPD', ctypes.c_uint16)
	]


# packet 0x215
class ZC_SKILLMSG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MsgNo', ctypes.c_uint32)
	]


# packet 0x216
class ZC_BABYMSG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MsgNo', ctypes.c_uint32)
	]


# packet 0x217
class CZ_BLACKSMITH_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x218
class CZ_ALCHEMIST_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x219
class ZC_BLACKSMITH_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Name', ctypes.c_char * 24),
		('Point', ctypes.c_uint32)
	]


# packet 0x21a
class ZC_ALCHEMIST_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Name', ctypes.c_char * 24),
		('Point', ctypes.c_uint32)
	]


# packet 0x21b
class ZC_BLACKSMITH_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Point', ctypes.c_uint32),
		('TotalPoint', ctypes.c_uint32)
	]


# packet 0x21c
class ZC_ALCHEMIST_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Point', ctypes.c_uint32),
		('TotalPoint', ctypes.c_uint32)
	]


# packet 0x21d
class CZ_LESSEFFECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('isLess', ctypes.c_uint32)
	]


# packet 0x21e
class ZC_LESSEFFECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('isLess', ctypes.c_uint32)
	]


# packet 0x21f
class ZC_NOTIFY_PKINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('winPoint', ctypes.c_uint32),
		('losePoint', ctypes.c_uint32),
		('killName', ctypes.c_char * 24),
		('killedName', ctypes.c_char * 24),
		('dwLowDateTime', ctypes.c_uint32),
		('dwHighDateTime', ctypes.c_uint32)
	]


# packet 0x220
class ZC_NOTIFY_CRAZYKILLER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('isCrazyKiller', ctypes.c_uint32)
	]

class ZC_NOTIFY_WEAPONITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]

# packet 0x221
class ZC_NOTIFY_WEAPONITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('weaponItemInfo', ZC_NOTIFY_WEAPONITEMLIST_SUB * 0)
    ]


# packet 0x222
class CZ_REQ_WEAPONREFINE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x223
class ZC_ACK_WEAPONREFINE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('msg', ctypes.c_uint32),
		('ITID', ctypes.c_uint16)
	]


# packet 0x224
class ZC_TAEKWON_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Point', ctypes.c_uint32),
		('TotalPoint', ctypes.c_uint32)
	]


# packet 0x225
class CZ_TAEKWON_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x226
class ZC_TAEKWON_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Name', ctypes.c_char * 24),
		('Point', ctypes.c_uint32)
	]


# packet 0x227
class ZC_GAME_GUARD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AuthData', ctypes.c_uint32)
	]


# packet 0x228
class CZ_ACK_GAME_GUARD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AuthData', ctypes.c_uint32)
	]


# packet 0x229
class ZC_STATE_CHANGE3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8)
	]


# packet 0x22a
class ZC_NOTIFY_STANDENTRY3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x22b
class ZC_NOTIFY_NEWENTRY3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x22c
class ZC_NOTIFY_MOVEENTRY3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16)
	]


# packet 0x22d
class CZ_COMMAND_MER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16),
		('command', ctypes.c_uint8)
	]


# packet 0x22e
class ZC_PROPERTY_HOMUN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('szName', ctypes.c_char * 24),
		('bModified', ctypes.c_uint8),
		('nLevel', ctypes.c_uint16),
		('nFullness', ctypes.c_uint16),
		('nRelationship', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('atk', ctypes.c_uint16),
		('Matk', ctypes.c_uint16),
		('hit', ctypes.c_uint16),
		('critical', ctypes.c_uint16),
		('_def', ctypes.c_uint16),
		('Mdef', ctypes.c_uint16),
		('flee', ctypes.c_uint16),
		('aspd', ctypes.c_uint16),
		('hp', ctypes.c_uint16),
		('maxHP', ctypes.c_uint16),
		('sp', ctypes.c_uint16),
		('maxSP', ctypes.c_uint16),
		('exp', ctypes.c_uint32),
		('maxEXP', ctypes.c_uint32),
		('SKPoint', ctypes.c_uint16),
		('ATKRange', ctypes.c_uint16)
	]


# packet 0x230
class ZC_CHANGESTATE_MER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('data', ctypes.c_uint32)
	]


# packet 0x231
class CZ_RENAME_MER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0x232
class CZ_REQUEST_MOVENPC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('dest', ctypes.c_char * 3)
	]


# packet 0x233
class CZ_REQUEST_ACTNPC(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('targetGID', ctypes.c_uint32),
		('action', ctypes.c_uint8)
	]


# packet 0x234
class CZ_REQUEST_MOVETOOWNER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x23a
class ZC_REQ_STORE_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Info', ctypes.c_uint16)
	]


# packet 0x23b
class CZ_ACK_STORE_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint16),
		('Password', ctypes.c_char * 16),
		('NewPassword', ctypes.c_char * 16)
	]


# packet 0x23c
class ZC_RESULT_STORE_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('ErrorCount', ctypes.c_uint16)
	]


# packet 0x23d
class AC_EVENT_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EventItemCount', ctypes.c_uint32)
	]


# packet 0x23e
class HC_REQUEST_CHARACTER_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('dummyValue', ctypes.c_uint32)
	]


# packet 0x23f
class CZ_MAIL_GET_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class ZC_MAIL_REQ_GET_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('MailID', ctypes.c_uint32),
		('HEADER', ctypes.c_char * 40),
		('isOpen', ctypes.c_uint8),
		('FromName', ctypes.c_char * 24),
		('DeleteTime', ctypes.c_uint32)
    ]

# packet 0x240
class ZC_MAIL_REQ_GET_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('MailNumber', ctypes.c_uint32),
        ('mailList', ZC_MAIL_REQ_GET_LIST_SUB * 10)
    ]

# packet 0x241
class CZ_MAIL_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32)
	]


# packet 0x242
class ZC_MAIL_REQ_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('MailID', ctypes.c_uint32),
		('Header', ctypes.c_char * 40),
		('FromName', ctypes.c_char * 24),
		('DeleteTime', ctypes.c_uint32),
		('Money', ctypes.c_uint32),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('Type', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('msg_len', ctypes.c_uint8),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x243
class CZ_MAIL_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32)
	]


# packet 0x244
class CZ_MAIL_GET_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32)
	]


# packet 0x245
class ZC_MAIL_REQ_GET_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x246
class CZ_MAIL_RESET_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint16)
	]


# packet 0x247
class CZ_MAIL_ADD_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x248
class CZ_MAIL_SEND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ReceiveName', ctypes.c_char * 24),
		('Header', ctypes.c_char * 40),
		('msg_len', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x249
class ZC_MAIL_REQ_SEND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x24a
class ZC_MAIL_RECEIVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32),
		('Header', ctypes.c_char * 40),
		('FromName', ctypes.c_char * 24)
	]


# packet 0x24b
class CZ_AUCTION_CREATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint16)
	]


# packet 0x24c
class CZ_AUCTION_ADD_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x24d
class CZ_AUCTION_ADD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NowMoney', ctypes.c_uint32),
		('MaxMoney', ctypes.c_uint32),
		('DeleteHour', ctypes.c_uint16)
	]


# packet 0x24e
class CZ_AUCTION_ADD_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AuctionID', ctypes.c_uint32)
	]


# packet 0x24f
class CZ_AUCTION_BUY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AuctionID', ctypes.c_uint32),
		('Money', ctypes.c_uint32)
	]


# packet 0x250
class ZC_AUCTION_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x251
class CZ_AUCTION_ITEM_SEARCH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint16),
		('AuctionID', ctypes.c_uint32),
		('Name', ctypes.c_char * 24),
		('Page', ctypes.c_uint16)
	]

class ZC_AUCTION_ITEM_REQ_SEARCH_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('AuctionID', ctypes.c_uint32),
		('SellerName', ctypes.c_char * 24),
		('ITID', ctypes.c_uint16),
		('Type', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('NowPrice', ctypes.c_uint32),
		('MaxPrice', ctypes.c_uint32),
		('BuyerName', ctypes.c_char * 24),
		('DeleteTime', ctypes.c_uint32),
    ]

# packet 0x252
class ZC_AUCTION_ITEM_REQ_SEARCH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('MaxPage', ctypes.c_uint32),
		('Number', ctypes.c_uint32),
        ('auctions', ZC_AUCTION_ITEM_REQ_SEARCH_SUB * 0)
    ]


# packet 0x253
class ZC_STARPLACE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('which', ctypes.c_uint8)
	]


# packet 0x254
class CZ_AGREE_STARPLACE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('which', ctypes.c_uint8)
	]


# packet 0x255
class ZC_ACK_MAIL_ADD_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x256
class ZC_ACK_AUCTION_ADD_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x257
class ZC_ACK_MAIL_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32),
		('Result', ctypes.c_uint16)
	]


# packet 0x258
class CA_REQ_GAME_GUARD_CHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x259
class AC_ACK_GAME_GUARD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ucAnswer', ctypes.c_uint8)
	]


# packet 0x25a
class ZC_MAKINGITEM_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('idList', ctypes.c_uint16)
	]


# packet 0x25b
class CZ_REQ_MAKINGITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('mkType', ctypes.c_uint16),
		('id', ctypes.c_uint16)
	]


# packet 0x25c
class CZ_AUCTION_REQ_MY_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint16)
	]


# packet 0x25d
class CZ_AUCTION_REQ_MY_SELL_STOP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AuctionID', ctypes.c_uint32)
	]


# packet 0x25e
class ZC_AUCTION_ACK_MY_SELL_STOP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x25f
class ZC_AUCTION_WINDOWS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint32)
	]


# packet 0x260
class ZC_MAIL_WINDOWS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint32)
	]


# packet 0x261
class AC_REQ_LOGIN_OLDEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_SeedValue', ctypes.c_char * 9)
	]


# packet 0x262
class AC_REQ_LOGIN_NEWEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_SeedValue', ctypes.c_char * 9)
	]


# packet 0x263
class AC_REQ_LOGIN_CARDPASS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_SeedValue', ctypes.c_char * 9)
	]


# packet 0x264
class CA_ACK_LOGIN_OLDEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_SeedValue', ctypes.c_char * 9),
		('m_EKey', ctypes.c_char * 9)
	]


# packet 0x265
class CA_ACK_LOGIN_NEWEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_SeedValue', ctypes.c_char * 9),
		('m_EKey', ctypes.c_char * 9)
	]


# packet 0x266
class CA_ACK_LOGIN_CARDPASS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_cardPass', ctypes.c_char * 28)
	]


# packet 0x267
class AC_ACK_EKEY_FAIL_NOTEXIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x268
class AC_ACK_EKEY_FAIL_NOTUSESEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x269
class AC_ACK_EKEY_FAIL_NOTUSEDEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x26a
class AC_ACK_EKEY_FAIL_AUTHREFUSE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x26b
class AC_ACK_EKEY_FAIL_INPUTEKEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x26c
class AC_ACK_EKEY_FAIL_NOTICE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x26d
class AC_ACK_EKEY_FAIL_NEEDCARDPASS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x26e
class AC_ACK_AUTHEKEY_FAIL_NOTMATCHCARDPASS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('errorCode', ctypes.c_uint16)
	]


# packet 0x26f
class AC_ACK_FIRST_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x270
class AC_REQ_LOGIN_ACCOUNT_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x271
class CA_ACK_LOGIN_ACCOUNT_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('sex', ctypes.c_uint16),
		('bPoint', ctypes.c_uint16),
		('E_mail', ctypes.c_char * 34)
	]


# packet 0x272
class AC_ACK_PT_ID_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('szPTID', ctypes.c_char * 21),
		('szPTNumID', ctypes.c_char * 21)
	]


# packet 0x273
class CZ_REQ_MAIL_RETURN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32),
		('ReceiveName', ctypes.c_char * 24)
	]


# packet 0x274
class ZC_ACK_MAIL_RETURN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MailID', ctypes.c_uint32),
		('Result', ctypes.c_uint16)
	]


# packet 0x275
class CH_ENTER2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('AuthCode', ctypes.c_uint32),
		('userLevel', ctypes.c_uint32),
		('clientType', ctypes.c_uint16),
		('Sex', ctypes.c_uint8),
		('macData', ctypes.c_char * 16),
		('iAccountSID', ctypes.c_uint32)
	]


# packet 0x276
class AC_ACCEPT_LOGIN2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AuthCode', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('userLevel', ctypes.c_uint32),
		('lastLoginIP', ctypes.c_uint32),
		('lastLoginTime', ctypes.c_char * 26),
		('Sex', ctypes.c_uint8),
		('iAccountSID', ctypes.c_uint32)
	]


# packet 0x277
class CA_LOGIN_PCBANG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('Passwd', ctypes.c_char * 24),
		('clienttype', ctypes.c_uint8),
		('IP', ctypes.c_char * 16),
		('MacAdress', ctypes.c_char * 13)
	]


# packet 0x278
class ZC_NOTIFY_PCBANG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x279
class CZ_HUNTINGLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class ZC_HUNTINGLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('questID', ctypes.c_uint32),
		('mobGID', ctypes.c_uint32),
		('maxCount', ctypes.c_uint16),
		('count', ctypes.c_uint16),
    ]
# packet 0x27a
class ZC_HUNTINGLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('huntingList', ZC_HUNTINGLIST_SUB * 0)
    ]


# packet 0x27b
class ZC_PCBANG_EFFECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ExpFactor', ctypes.c_uint32),
		('ExpFactor2', ctypes.c_uint32),
		('DropFactor', ctypes.c_uint32)
	]


# packet 0x27c
class CA_LOGIN4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('PasswdMD5', ctypes.c_char * 16),
		('clienttype', ctypes.c_uint8),
		('macData', ctypes.c_char * 13)
	]


# packet 0x27d
class ZC_PROPERTY_MERCE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('level', ctypes.c_uint16),
		('faith', ctypes.c_uint16),
		('summonCount', ctypes.c_uint16),
		('atk', ctypes.c_uint16),
		('Matk', ctypes.c_uint16),
		('hit', ctypes.c_uint16),
		('critical', ctypes.c_uint16),
		('_def', ctypes.c_uint16),
		('Mdef', ctypes.c_uint16),
		('flee', ctypes.c_uint16),
		('aspd', ctypes.c_uint16),
		('hp', ctypes.c_uint16),
		('maxHP', ctypes.c_uint16),
		('sp', ctypes.c_uint16),
		('maxSP', ctypes.c_uint16),
		('ATKRange', ctypes.c_uint16),
		('exp', ctypes.c_uint32)
	]


# packet 0x27e
class ZC_SHANDA_PROTECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('CodeLen', ctypes.c_uint16),
		('Code', ctypes.c_char * 255)
    ]


# packet 0x27f
class CA_CLIENT_TYPE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ClientType', ctypes.c_uint16),
		('nVer', ctypes.c_uint32)
	]


# packet 0x280
class ZC_GANGSI_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Point', ctypes.c_uint32),
		('TotalPoint', ctypes.c_uint32),
		('PacketSwitch', ctypes.c_uint16)
	]


# packet 0x281
class CZ_GANGSI_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketSwitch', ctypes.c_uint16)
	]


# packet 0x282
class ZC_GANGSI_RANK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Name', ctypes.c_char * 24),
		('Point', ctypes.c_uint32),
		('PacketSwitch', ctypes.c_uint16)
	]


# packet 0x283
class ZC_AID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x284
class ZC_NOTIFY_EFFECT3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('effectID', ctypes.c_uint32),
		('numdata', ctypes.c_uint32)
	]


# packet 0x285
class ZC_DEATH_QUESTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Qcategory', ctypes.c_uint16),
		('Qnum', ctypes.c_uint16)
	]


# packet 0x286
class CZ_DEATH_QUESTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Qanswer', ctypes.c_uint16)
	]

class ZC_PC_CASH_POINT_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('price', ctypes.c_uint32),
		('discountprice', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
    ]
# packet 0x287
class ZC_PC_CASH_POINT_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('CashPoint', ctypes.c_uint32),
        ('itemList', ZC_PC_CASH_POINT_ITEMLIST_SUB * 0)
    ]


# packet 0x288
class CZ_PC_BUY_CASH_POINT_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0x289
class ZC_PC_CASH_POINT_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CashPoint', ctypes.c_uint32),
		('Error', ctypes.c_uint16)
	]


# packet 0x28a
class ZC_NPC_SHOWEFST_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('effectState', ctypes.c_uint32),
		('clevel', ctypes.c_uint32),
		('showEFST', ctypes.c_uint32)
	]


# packet 0x28c
class CH_SELECT_CHAR_GOINGTOBEUSED(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dwAID', ctypes.c_uint32),
		('nCountSelectedChar', ctypes.c_uint32),
		('ardwSelectedGID', ctypes.c_uint32)
	]


# packet 0x28d
class CH_REQ_IS_VALID_CHARNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dwAID', ctypes.c_uint32),
		('dwGID', ctypes.c_uint32),
		('szCharName', ctypes.c_char * 24)
	]


# packet 0x28e
class HC_ACK_IS_VALID_CHARNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('sResult', ctypes.c_uint16)
	]


# packet 0x28f
class CH_REQ_CHANGE_CHARNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dwGID', ctypes.c_uint32)
	]


# packet 0x290
class HC_ACK_CHANGE_CHARNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('sResult', ctypes.c_uint16)
	]


# packet 0x291
class ZC_MSG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('msg', ctypes.c_uint16)
	]


# packet 0x292
class CZ_STANDING_RESURRECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x293
class ZC_BOSS_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('infoType', ctypes.c_uint8),
		('xPos', ctypes.c_uint32),
		('yPos', ctypes.c_uint32),
		('minHour', ctypes.c_uint16),
		('minMinute', ctypes.c_uint16),
		('maxHour', ctypes.c_uint16),
		('maxMinute', ctypes.c_uint16),
		('name', ctypes.c_char * 51)
	]


# packet 0x294
class ZC_READ_BOOK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('bookID', ctypes.c_uint32),
		('page', ctypes.c_uint32)
	]

class ZC_EQUIPMENT_ITEMLIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
    ]

# packet 0x295
class ZC_EQUIPMENT_ITEMLIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_EQUIPMENT_ITEMLIST2_SUB * 0),
    ]


class ZC_STORE_EQUIPMENT_ITEMLIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
    ]

# packet 0x296
class ZC_STORE_EQUIPMENT_ITEMLIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_STORE_EQUIPMENT_ITEMLIST2_SUB * 0),
    ]

class ZC_CART_EQUIPMENT_ITEMLIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
    ]
		
# packet 0x297
class ZC_CART_EQUIPMENT_ITEMLIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_CART_EQUIPMENT_ITEMLIST2_SUB * 0),
    ]


# packet 0x298
class ZC_CASH_TIME_COUNTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('RemainSecond', ctypes.c_uint32)
	]


# packet 0x299
class ZC_CASH_ITEM_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16)
	]


# packet 0x29a
class ZC_ITEM_PICKUP_ACK2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('location', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8),
		('HireExpireDate', ctypes.c_uint32)
	]


# packet 0x29b
class ZC_MER_INIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('atk', ctypes.c_uint16),
		('Matk', ctypes.c_uint16),
		('hit', ctypes.c_uint16),
		('critical', ctypes.c_uint16),
		('_def', ctypes.c_uint16),
		('Mdef', ctypes.c_uint16),
		('flee', ctypes.c_uint16),
		('aspd', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('level', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxHP', ctypes.c_uint32),
		('sp', ctypes.c_uint32),
		('maxSP', ctypes.c_uint32),
		('ExpireDate', ctypes.c_uint32),
		('faith', ctypes.c_uint16),
		('toal_call_num', ctypes.c_uint32),
		('approval_monster_kill_counter', ctypes.c_uint32),
		('ATKRange', ctypes.c_uint16)
	]


# packet 0x29c
class ZC_MER_PROPERTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('atk', ctypes.c_uint16),
		('Matk', ctypes.c_uint16),
		('hit', ctypes.c_uint16),
		('critical', ctypes.c_uint16),
		('_def', ctypes.c_uint16),
		('Mdef', ctypes.c_uint16),
		('flee', ctypes.c_uint16),
		('aspd', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('level', ctypes.c_uint16),
		('hp', ctypes.c_uint16),
		('maxHP', ctypes.c_uint16),
		('sp', ctypes.c_uint16),
		('maxSP', ctypes.c_uint16),
		('ExpireDate', ctypes.c_uint32),
		('faith', ctypes.c_uint16),
		('toal_call_num', ctypes.c_uint32),
		('approval_monster_kill_counter', ctypes.c_uint32)
	]

class ZC_MER_SKILLINFO_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('SKID', ctypes.c_uint16),
		('type', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('skillName', ctypes.c_char * 24),
		('upgradable', ctypes.c_uint8),
    ]
# packet 0x29d
class ZC_MER_SKILLINFO_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('skillinfoList', ZC_MER_SKILLINFO_LIST_SUB * 0),
    ]


# packet 0x29e
class ZC_MER_SKILLINFO_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('upgradable', ctypes.c_uint8)
	]


# packet 0x29f
class CZ_MER_COMMAND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('command', ctypes.c_uint8)
	]


# packet 0x2a0
class CZ_MER_USE_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('targetID', ctypes.c_uint32)
	]


class CZ_MER_UPGRADE_SKILLLEVEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
		('SKID', ctypes.c_uint16)
    ]


# packet 0x2a2
class ZC_MER_PAR_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('var', ctypes.c_uint16),
		('value', ctypes.c_uint32)
	]


# packet 0x2a3
class ZC_GAMEGUARD_LINGO_KEY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('packetType', ctypes.c_uint16),
		('dwAlgNum', ctypes.c_uint32),
		('dwAlgKey1', ctypes.c_uint32),
		('dwAlgKey2', ctypes.c_uint32),
		('dwSeed', ctypes.c_uint32)
	]


# packet 0x2a5
class CZ_KSY_EVENT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x2aa
class ZC_REQ_CASH_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Info', ctypes.c_uint16)
	]


# packet 0x2ab
class CZ_ACK_CASH_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint16),
		('Password', ctypes.c_char * 16),
		('NewPassword', ctypes.c_char * 16)
	]


# packet 0x2ac
class ZC_RESULT_CASH_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('ErrorCount', ctypes.c_uint16)
	]


# packet 0x2ad
class AC_REQUEST_SECOND_PASSWORD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('dwSeed', ctypes.c_uint32)
	]


# packet 0x2b0
class CA_LOGIN_HAN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('Passwd', ctypes.c_char * 24),
		('clienttype', ctypes.c_uint8),
		('m_szIP', ctypes.c_char * 16),
		('m_szMacAddr', ctypes.c_char * 13),
		('isHanGameUser', ctypes.c_uint8)
	]

class ZC_ALL_QUEST_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8),
    ]
# packet 0x2b1
class ZC_ALL_QUEST_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('questCount', ctypes.c_uint32),
        ('questList', ZC_ALL_QUEST_LIST_SUB * 0),
    ]

class ZC_ALL_QUEST_MISSION_MOBS_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('mobGID', ctypes.c_uint32),
		('huntCount', ctypes.c_uint16),
		('mobName', ctypes.c_char * 24),
    ]
class ZC_ALL_QUEST_MISSION_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('questID', ctypes.c_uint32),
		('quest_svrTime', ctypes.c_uint32),
		('quest_endTime', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('mobList', ZC_ALL_QUEST_MISSION_MOBS_SUB * 0)
    ]

# packet 0x2b2
class ZC_ALL_QUEST_MISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('count', ctypes.c_uint32),
        ('questList', ZC_ALL_QUEST_MISSION_SUB * 0)
    ]

class ZC_ADD_QUEST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('mobGID', ctypes.c_uint32),
		('huntCount', ctypes.c_uint16),
		('mobName', ctypes.c_char * 24)
    ]
# packet 0x2b3
class ZC_ADD_QUEST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8),
		('quest_svrTime', ctypes.c_uint32),
		('quest_endTime', ctypes.c_uint32),
		('count', ctypes.c_uint16),
        ('mobList', ZC_ADD_QUEST_SUB * 0)
    ]


# packet 0x2b4
class ZC_DEL_QUEST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('questID', ctypes.c_uint32)
	]

class ZC_UPDATE_MISSION_HUNT_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('questID', ctypes.c_uint32),
		('mobGID', ctypes.c_uint32),
		('maxCount', ctypes.c_uint16),
		('count', ctypes.c_uint16)
    ]

# packet 0x2b5
class ZC_UPDATE_MISSION_HUNT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('count', ctypes.c_uint16),
        ('mobList', ZC_UPDATE_MISSION_HUNT_SUB * 0)
    ]


# packet 0x2b6
class CZ_ACTIVE_QUEST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8)
	]


# packet 0x2b7
class ZC_ACTIVE_QUEST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8)
	]


# packet 0x2b8
class ZC_ITEM_PICKUP_PARTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('accountID', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('location', ctypes.c_uint16),
		('type', ctypes.c_uint8)
	]

class ZC_SHORTCUT_KEY_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('isSkill', ctypes.c_uint8),
		('ID', ctypes.c_uint32),
		('count', ctypes.c_uint16),
    ]

# packet 0x2b9
class ZC_SHORTCUT_KEY_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
        ('keyList', ZC_SHORTCUT_KEY_LIST_SUB * 0)
    ]

# packet 0x2ba
class CZ_SHORTCUT_KEY_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('isSkill', ctypes.c_uint8),
		('ID', ctypes.c_uint32),
		('count', ctypes.c_uint16)
	]


# packet 0x2bb
class ZC_EQUIPITEM_DAMAGED(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint16),
		('accountID', ctypes.c_uint32)
	]


# packet 0x2bc
class ZC_NOTIFY_PCBANG_PLAYING_TIME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('TimeMinute', ctypes.c_uint32)
	]


# packet 0x2bf
class ZC_SRPACKETR2_INIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ProtectFactor', ctypes.c_uint16),
		('DeformSeedFactor', ctypes.c_uint32),
		('DeformAddFactor', ctypes.c_uint32)
	]


# packet 0x2c0
class CZ_SRPACKETR2_START(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ProtectFactor', ctypes.c_uint16)
	]


# packet 0x2c1
class ZC_NPC_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('accountID', ctypes.c_uint32),
		('color', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x2c2
class ZC_FORMATSTRING_MSG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_uint16),
		('value', ctypes.c_char * 255)
    ]


# packet 0x2c4
class CZ_PARTY_JOIN_REQ(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24)
	]


# packet 0x2c5
class ZC_PARTY_JOIN_REQ_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24),
		('answer', ctypes.c_uint32)
	]


# packet 0x2c6
class ZC_PARTY_JOIN_REQ(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GRID', ctypes.c_uint32),
		('groupName', ctypes.c_char * 24)
	]


# packet 0x2c7
class CZ_PARTY_JOIN_REQ_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GRID', ctypes.c_uint32),
		('bAccept', ctypes.c_uint8)
	]


# packet 0x2c8
class CZ_PARTY_CONFIG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('bRefuseJoinMsg', ctypes.c_uint8)
	]


# packet 0x2c9
class ZC_PARTY_CONFIG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('bRefuseJoinMsg', ctypes.c_uint8)
	]


# packet 0x2ca
class HC_REFUSE_SELECTCHAR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8)
	]


# packet 0x2cb
class ZC_MEMORIALDUNGEON_SUBSCRIPTION_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MemorialDungeonName', ctypes.c_char * 61),
		('PriorityOrderNum', ctypes.c_uint16)
	]


# packet 0x2cc
class ZC_MEMORIALDUNGEON_SUBSCRIPTION_NOTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PriorityOrderNum', ctypes.c_uint16)
	]


# packet 0x2cd
class ZC_MEMORIALDUNGEON_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('MemorialDungeonName', ctypes.c_char * 61),
		('DestroyDate', ctypes.c_uint32),
		('EnterTimeOutDate', ctypes.c_uint32)
	]


# packet 0x2ce
class ZC_MEMORIALDUNGEON_NOTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint32),
		('EnterLimitDate', ctypes.c_uint32)
	]


# packet 0x2cf
class CZ_MEMORIALDUNGEON_COMMAND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Command', ctypes.c_uint32)
	]

class ZC_EQUIPMENT_ITEMLIST3_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16)
    ]
# packet 0x2d0
class ZC_EQUIPMENT_ITEMLIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('equipmentList', ZC_EQUIPMENT_ITEMLIST3_SUB * 0)
    ]

class ZC_STORE_EQUIPMENT_ITEMLIST3_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16)
    ]
# packet 0x2d1
class ZC_STORE_EQUIPMENT_ITEMLIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('equipmentList', ZC_STORE_EQUIPMENT_ITEMLIST3_SUB * 0)
    ]

class ZC_CART_EQUIPMENT_ITEMLIST3_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
    ]
		
# packet 0x2d2
class ZC_CART_EQUIPMENT_ITEMLIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('equipmentList', ZC_CART_EQUIPMENT_ITEMLIST3_SUB * 0)
    ]


# packet 0x2d3
class ZC_NOTIFY_BIND_ON_EQUIP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16)
	]


# packet 0x2d4
class ZC_ITEM_PICKUP_ACK3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('location', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16)
	]


# packet 0x2d5
class ZC_ISVR_DISCONNECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x2d6
class CZ_EQUIPWIN_MICROSCOPE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]

class ZC_EQUIPWIN_MICROSCOPE_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('IsDamaged', ctypes.c_uint8),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
    ]
# packet 0x2d7
class ZC_EQUIPWIN_MICROSCOPE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('sex', ctypes.c_uint8),
        ('itemInfo', ZC_EQUIPWIN_MICROSCOPE_ITEMINFO * 0)
    ]


# packet 0x2d8
class CZ_CONFIG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Config', ctypes.c_uint32),
		('Value', ctypes.c_uint32)
	]


# packet 0x2d9
class ZC_CONFIG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Config', ctypes.c_uint32),
		('Value', ctypes.c_uint32)
	]


# packet 0x2da
class ZC_CONFIG_NOTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('bOpenEquipmentWin', ctypes.c_uint8)
	]


# packet 0x2db
class CZ_BATTLEFIELD_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x2dc
class ZC_BATTLEFIELD_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('accountID', ctypes.c_uint32),
		('name', ctypes.c_char * 24),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x2dd
class ZC_BATTLEFIELD_NOTIFY_CAMPINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('accountID', ctypes.c_uint32),
		('name', ctypes.c_char * 24),
		('camp', ctypes.c_uint16)
	]


# packet 0x2de
class ZC_BATTLEFIELD_NOTIFY_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('pointCampA', ctypes.c_uint16),
		('pointCampB', ctypes.c_uint16)
	]


# packet 0x2df
class ZC_BATTLEFIELD_NOTIFY_POSITION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('accountID', ctypes.c_uint32),
		('name', ctypes.c_char * 24),
		('job', ctypes.c_uint16),
		('x', ctypes.c_uint16),
		('y', ctypes.c_uint16)
	]


# packet 0x2e0
class ZC_BATTLEFIELD_NOTIFY_HP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('accountID', ctypes.c_uint32),
		('name', ctypes.c_char * 24),
		('hp', ctypes.c_uint16),
		('maxHp', ctypes.c_uint16)
	]


# packet 0x2e1
class ZC_NOTIFY_ACT2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('targetGID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('attackMT', ctypes.c_uint32),
		('attackedMT', ctypes.c_uint32),
		('damage', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8),
		('leftDamage', ctypes.c_uint32)
	]


# packet 0x2e6
class CZ_BOT_CHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('IsBot', ctypes.c_uint32)
	]


# packet 0x2e7
class ZC_MAPPROPERTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('type', ctypes.c_uint16),
		('mapInfoTable', ctypes.c_uint32)
	]

class ZC_NORMAL_ITEMLIST3_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
    ]
# packet 0x2e8
class ZC_NORMAL_ITEMLIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ItemInfo', ZC_NORMAL_ITEMLIST3_ITEMINFO * 0)
    ]


class ZC_CART_NORMAL_ITEMLIST3_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32)
    ]
# packet 0x2e9
class ZC_CART_NORMAL_ITEMLIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('ItemInfo', ZC_CART_NORMAL_ITEMLIST3_ITEMINFO * 0)
    ]


class ZC_STORE_NORMAL_ITEMLIST3_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
    ]
# packet 0x2ea
class ZC_STORE_NORMAL_ITEMLIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('ItemInfo', ZC_STORE_NORMAL_ITEMLIST3_ITEMINFO * 0)
    ]


# packet 0x2eb
class ZC_ACCEPT_ENTER2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('startTime', ctypes.c_uint32),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('font', ctypes.c_uint16)
	]


# packet 0x2ec
class ZC_NOTIFY_MOVEENTRY4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16)
	]


# packet 0x2ed
class ZC_NOTIFY_NEWENTRY4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16)
	]


# packet 0x2ee
class ZC_NOTIFY_STANDENTRY4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16)
	]


# packet 0x2ef
class ZC_NOTIFY_FONT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('font', ctypes.c_uint16)
	]


# packet 0x2f0
class ZC_PROGRESS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('color', ctypes.c_uint32),
		('time', ctypes.c_uint32)
	]


# packet 0x2f1
class CZ_PROGRESS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x2f2
class ZC_PROGRESS_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x2f3
class CZ_IRMAIL_SEND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ReceiveName', ctypes.c_char * 24),
		('Title', ctypes.c_char * 40),
		('Zeny', ctypes.c_uint32),
		('index', ctypes.c_uint16),
		('id', ctypes.c_uint16),
		('cnt', ctypes.c_uint16)
	]


# packet 0x2f4
class ZC_IRMAIL_SEND_RES(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x2f5
class ZC_IRMAIL_NOTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('office', ctypes.c_uint8),
		('id', ctypes.c_uint32)
	]


# packet 0x2f6
class CZ_IRMAIL_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('office', ctypes.c_uint8),
		('id', ctypes.c_uint32)
	]


# packet 0x35c
class CZ_OPEN_SIMPLE_CASHSHOP_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST_ITEM(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('price', ctypes.c_uint32),
		('discountprice', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
    ]
# packet 0x35d
class ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('CashPoint', ctypes.c_uint32),
		('md_itemcount', ctypes.c_uint16),
		('md_itemSize', ctypes.c_uint16),
		('best_itemcount', ctypes.c_uint16),
		('best_itemsize', ctypes.c_uint16),
        ('md_item', ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST_ITEM * 0),
    ]


# packet 0x35e
class CZ_CLOSE_WINDOW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x35f
class CZ_REQUEST_MOVE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dest', ctypes.c_char * 3)
	]


# packet 0x360
class CZ_REQUEST_TIME2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('clientTime', ctypes.c_uint32)
	]


# packet 0x361
class CZ_CHANGE_DIRECTION2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('dir', ctypes.c_uint8)
	]


# packet 0x362
class CZ_ITEM_PICKUP2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32)
	]


# packet 0x363
class CZ_ITEM_THROW2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0x364
class CZ_MOVE_ITEM_FROM_BODY_TO_STORE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x365
class CZ_MOVE_ITEM_FROM_STORE_TO_BODY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x366
class CZ_USE_SKILL_TOGROUND2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x367
class CZ_USE_SKILL_TOGROUND_WITHTALKBOX2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('contents', ctypes.c_char * 80)
	]


# packet 0x368
class CZ_REQNAME2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x369
class CZ_REQNAME_BYGID2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x3de
class CAH_ACK_GAME_GUARD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AuthData', ctypes.c_uint32)
	]


# packet 0x436
class CZ_ENTER2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('AuthCode', ctypes.c_uint32),
		('clientTime', ctypes.c_uint32),
		('Sex', ctypes.c_uint8)
	]


# packet 0x437
class CZ_REQUEST_ACT2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('targetGID', ctypes.c_uint32),
		('action', ctypes.c_uint8)
	]


# packet 0x438
class CZ_USE_SKILL2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('targetID', ctypes.c_uint32)
	]


# packet 0x439
class CZ_USE_ITEM2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x43d
class ZC_SKILL_POSTDELAY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('DelayTM', ctypes.c_uint32)
	]

class ZC_SKILL_POSTDELAY_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('SKID', ctypes.c_uint16),
		('DelayTM', ctypes.c_uint32),
    ]
# packet 0x43e
class ZC_SKILL_POSTDELAY_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('skillList', ZC_SKILL_POSTDELAY_LIST_SUB * 0),
    ]


# packet 0x43f
class ZC_MSG_STATE_CHANGE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('state', ctypes.c_uint8),
		('RemainMS', ctypes.c_uint32),
		('val', ctypes.c_uint32)
	]


# packet 0x440
class ZC_MILLENNIUMSHIELD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('num', ctypes.c_uint16),
		('state', ctypes.c_uint16)
	]


# packet 0x441
class ZC_SKILLINFO_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16)
	]


# packet 0x442
class ZC_SKILL_SELECT_REQUEST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('why', ctypes.c_uint32),
		('SKIDList', ctypes.c_uint16)
	]


# packet 0x443
class CZ_SKILL_SELECT_RESPONSE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('why', ctypes.c_uint32),
		('SKID', ctypes.c_uint16)
	]

class ZC_SIMPLE_CASH_POINT_ITEMLIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('price', ctypes.c_uint32),
		('discountprice', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
    ]
# packet 0x444
class ZC_SIMPLE_CASH_POINT_ITEMLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('CashPoint', ctypes.c_uint32),
        ('itemList', ZC_SIMPLE_CASH_POINT_ITEMLIST_SUB * 0),
    ]


# packet 0x445
class CZ_SIMPLE_BUY_CASH_POINT_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0x446
class ZC_QUEST_NOTIFY_EFFECT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('npcID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('effect', ctypes.c_uint16),
		('type', ctypes.c_uint16)
	]


# packet 0x447
class CZ_BLOCKING_PLAY_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class HC_CHARACTER_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('dwGID', ctypes.c_uint32),
		('SlotIdx', ctypes.c_uint8)
    ]
# packet 0x448
class HC_CHARACTER_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('characterList', HC_CHARACTER_LIST_SUB * 0),
    ]


# packet 0x449
class ZC_HACKSH_ERROR_MSG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorID', ctypes.c_uint16)
	]


# packet 0x44a
class CZ_CLIENT_VERSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('clientVer', ctypes.c_uint32)
	]


# packet 0x44b
class CZ_CLOSE_SIMPLECASH_SHOP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x7d0
class ZC_ES_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('esNo', ctypes.c_uint16),
		('esMsg', ctypes.c_uint16)
	]


# packet 0x7d1
class CZ_ES_GET_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x7d2
class ZC_ES_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Count', ctypes.c_uint16)
	]


# packet 0x7d3
class CZ_ES_CHOOSE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('esNo', ctypes.c_uint16)
	]


# packet 0x7d4
class CZ_ES_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('esNo', ctypes.c_uint16)
	]


# packet 0x7d5
class ZC_ES_READY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('esNo', ctypes.c_uint16)
	]


# packet 0x7d6
class ZC_ES_GOTO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('esNo', ctypes.c_uint16)
	]


# packet 0x7d7
class CZ_GROUPINFO_CHANGE_V2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('expOption', ctypes.c_uint32),
		('ItemPickupRule', ctypes.c_uint8),
		('ItemDivisionRule', ctypes.c_uint8)
	]


# packet 0x7d8
class ZC_REQ_GROUPINFO_CHANGE_V2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('expOption', ctypes.c_uint32),
		('ItemPickupRule', ctypes.c_uint8),
		('ItemDivisionRule', ctypes.c_uint8)
	]

class ZC_SHORTCUT_KEY_LIST_V2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('isSkill', ctypes.c_uint8),
		('ID', ctypes.c_uint32),
		('count', ctypes.c_uint16),
    ]
# packet 0x7d9
class ZC_SHORTCUT_KEY_LIST_V2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
        ('keyList', ZC_SHORTCUT_KEY_LIST_V2_SUB * 0),
    ]


# packet 0x7da
class CZ_CHANGE_GROUP_MASTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x7db
class ZC_HO_PAR_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('var', ctypes.c_uint16),
		('value', ctypes.c_uint32)
	]


# packet 0x7dc
class CZ_SEEK_PARTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Option', ctypes.c_uint32)
	]


# packet 0x7dd
class ZC_SEEK_PARTY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Name', ctypes.c_char * 24),
		('Job', ctypes.c_uint32),
		('Level', ctypes.c_uint32),
		('mapName', ctypes.c_char * 16),
		('Option', ctypes.c_uint32)
	]


# packet 0x7de
class CZ_SEEK_PARTY_MEMBER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Job', ctypes.c_uint32),
		('Level', ctypes.c_uint32),
		('mapName', ctypes.c_char * 16),
		('Option', ctypes.c_uint32)
	]


# packet 0x7df
class ZC_SEEK_PARTY_MEMBER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Name', ctypes.c_char * 24),
		('Job', ctypes.c_uint32),
		('Level', ctypes.c_uint32),
		('mapName', ctypes.c_char * 16),
		('Option', ctypes.c_uint32)
	]


# packet 0x7e0
class ZC_ES_NOTI_MYINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('esNo', ctypes.c_uint16),
		('esname', ctypes.c_char * 54)
	]


# packet 0x7e1
class ZC_SKILLINFO_UPDATE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('type', ctypes.c_uint32),
		('level', ctypes.c_uint16),
		('spcost', ctypes.c_uint16),
		('attackRange', ctypes.c_uint16),
		('upgradable', ctypes.c_uint8)
	]


# packet 0x7e2
class ZC_MSG_VALUE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('msg', ctypes.c_uint16),
		('value', ctypes.c_uint32)
	]


# packet 0x7e3
class ZC_ITEMLISTWIN_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint32)
	]


# packet 0x7e4
class CZ_ITEMLISTWIN_RES(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Type', ctypes.c_uint32),
		('Action', ctypes.c_uint32),
		('MaterialList', ctypes.c_uint16)
	]


# packet 0x7e5
class CH_ENTER_CHECKBOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('dwAID', ctypes.c_uint32),
		('szStringInfo', ctypes.c_char * 255)
    ]


# packet 0x7e6
class ZC_MSG_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('MSGID', ctypes.c_uint32)
	]


# packet 0x7e7
class CH_CHECKBOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('dwAID', ctypes.c_uint32),
		('szStringInfo', ctypes.c_char * 24)
	]


# packet 0x7e8
class HC_CHECKBOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('img', ctypes.c_char * 255)
    ]


# packet 0x7e9
class HC_CHECKBOT_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x7ea
class CZ_BATTLE_FIELD_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class ZC_BATTLE_FIELD_LIST_INFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('BFNO', ctypes.c_uint32),
		('BattleFieldName', ctypes.c_char * 56),
		('JoinTeam', ctypes.c_uint16),
    ]
# packet 0x7eb
class ZC_BATTLE_FIELD_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Count', ctypes.c_uint16),
		('ack_type', ctypes.c_uint16),
        ('BattleFieldList', ZC_BATTLE_FIELD_LIST_INFO * 10)
    ]


# packet 0x7ec
class CZ_JOIN_BATTLE_FIELD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32),
		('JoinTeam', ctypes.c_uint16)
	]


# packet 0x7ed
class ZC_JOIN_BATTLE_FIELD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32),
		('JoinTeam', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x7ee
class CZ_CANCEL_BATTLE_FIELD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32)
	]


# packet 0x7ef
class ZC_CANCEL_BATTLE_FIELD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32),
		('Result', ctypes.c_uint16)
	]


# packet 0x7f0
class CZ_REQ_BATTLE_STATE_MONITOR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32),
		('PowerSwitch', ctypes.c_uint16)
	]


# packet 0x7f1
class ZC_ACK_BATTLE_STATE_MONITOR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32),
		('PlayCount', ctypes.c_uint16),
		('BattleState', ctypes.c_uint16),
		('TeamCount_A', ctypes.c_uint16),
		('TeamCount_B', ctypes.c_uint16),
		('MyCount', ctypes.c_uint16),
		('JoinTeam', ctypes.c_uint16)
	]


# packet 0x7f2
class ZC_BATTLE_NOTI_START_STEP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32),
		('Result', ctypes.c_uint16)
	]


# packet 0x7f3
class ZC_BATTLE_JOIN_NOTI_DEFER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('BFNO', ctypes.c_uint32)
	]


# packet 0x7f4
class ZC_BATTLE_JOIN_DISABLE_STATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Enable', ctypes.c_uint8)
	]


# packet 0x7f5
class CZ_GM_FULLSTRIP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('TargetAID', ctypes.c_uint32)
	]


# packet 0x7f6
class ZC_NOTIFY_EXP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('amount', ctypes.c_uint32),
		('varID', ctypes.c_uint16),
		('expType', ctypes.c_uint16)
	]


# packet 0x7f7
class ZC_NOTIFY_MOVEENTRY7(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0x7f8
class ZC_NOTIFY_NEWENTRY5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0x7f9
class ZC_NOTIFY_STANDENTRY5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('name', ctypes.c_char * 24)
	]


# packet 0x7fa
class ZC_DELETE_ITEM_FROM_BODY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('DeleteType', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('Count', ctypes.c_uint16)
	]


# packet 0x7fb
class ZC_USESKILL_ACK2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('targetID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('property', ctypes.c_uint32),
		('delayTime', ctypes.c_uint32),
		('isDisposable', ctypes.c_uint8)
	]


# packet 0x7fc
class ZC_CHANGE_GROUP_MASTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('OldMasterAID', ctypes.c_uint32),
		('NewMasterAID', ctypes.c_uint32)
	]


# packet 0x7fe
class ZC_PLAY_NPC_BGM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Bgm', ctypes.c_char * 24)
	]


# packet 0x7ff
class ZC_DEFINE_CHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Result', ctypes.c_uint32)
	]

class ZC_PC_PURCHASE_ITEMLIST_FROMMC2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('price', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]
		
# packet 0x800
class ZC_PC_PURCHASE_ITEMLIST_FROMMC2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('UniqueID', ctypes.c_uint32),
        ('itemList', ZC_PC_PURCHASE_ITEMLIST_FROMMC2_SUB * 1),
    ]

class CZ_PC_PURCHASE_ITEMLIST_FROMMC2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('count', ctypes.c_uint16),
		('index', ctypes.c_uint16),
    ]
# packet 0x801
class CZ_PC_PURCHASE_ITEMLIST_FROMMC2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('UniqueID', ctypes.c_uint32),
		('itemList', CZ_PC_PURCHASE_ITEMLIST_FROMMC2_SUB * 1),
    ]
		


# packet 0x802
class CZ_PARTY_BOOKING_REQ_REGISTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Level', ctypes.c_uint16),
		('MapID', ctypes.c_uint16),
		('Job', ctypes.c_uint16)
	]


# packet 0x803
class ZC_PARTY_BOOKING_ACK_REGISTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x804
class CZ_PARTY_BOOKING_REQ_SEARCH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Level', ctypes.c_uint16),
		('MapID', ctypes.c_uint16),
		('Job', ctypes.c_uint16),
		('LastIndex', ctypes.c_uint32),
		('ResultCount', ctypes.c_uint16)
	]

class ZC_PARTY_BOOKING_ACK_SEARCH_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('Index', ctypes.c_uint32),
		('CharName', ctypes.c_char * 24),
		('ExpireTime', ctypes.c_uint32),
		('Level', ctypes.c_uint16),
		('MapID', ctypes.c_uint16),
		('Job', ctypes.c_uint16),
    ]

# packet 0x805
class ZC_PARTY_BOOKING_ACK_SEARCH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('IsExistMoreResult', ctypes.c_uint8),
        ('searchInfoList', ZC_PARTY_BOOKING_ACK_SEARCH_SUB * 1),
    ]


# packet 0x806
class CZ_PARTY_BOOKING_REQ_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x807
class ZC_PARTY_BOOKING_ACK_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x808
class CZ_PARTY_BOOKING_REQ_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Job', ctypes.c_uint16)
	]


# packet 0x809
class ZC_PARTY_BOOKING_NOTIFY_INSERT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32),
		('CharName', ctypes.c_char * 24),
		('ExpireTime', ctypes.c_uint32),
		('Level', ctypes.c_uint16),
		('MapID', ctypes.c_uint16),
		('Job1', ctypes.c_uint16),
		('Job2', ctypes.c_uint16),
		('Job3', ctypes.c_uint16),
		('Job4', ctypes.c_uint16),
		('Job5', ctypes.c_uint16),
		('Job6', ctypes.c_uint16)
	]


# packet 0x80a
class ZC_PARTY_BOOKING_NOTIFY_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32),
		('Job1', ctypes.c_uint16),
		('Job2', ctypes.c_uint16),
		('Job3', ctypes.c_uint16),
		('Job4', ctypes.c_uint16),
		('Job5', ctypes.c_uint16),
		('Job6', ctypes.c_uint16)
	]


# packet 0x80b
class ZC_PARTY_BOOKING_NOTIFY_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x80c
class CZ_SIMPLE_CASH_BTNSHOW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x80d
class ZC_SIMPLE_CASH_BTNSHOW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('show', ctypes.c_uint8)
	]


# packet 0x80e
class ZC_NOTIFY_HP_TO_GROUPM_R2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('hp', ctypes.c_uint32),
		('maxhp', ctypes.c_uint32)
	]


# packet 0x80f
class ZC_ADD_EXCHANGE_ITEM2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('count', ctypes.c_uint32),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16)
	]


# packet 0x810
class ZC_OPEN_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('count', ctypes.c_uint8)
	]

class CZ_REQ_OPEN_BUYING_STORE_ITEMLIST(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('ITID', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('price', ctypes.c_uint32),
    ]
# packet 0x811
class CZ_REQ_OPEN_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('LimitZeny', ctypes.c_uint32),
		('result', ctypes.c_uint8),
		('storeName', ctypes.c_char * 80),
		('itemList', CZ_REQ_OPEN_BUYING_STORE_ITEMLIST * 0)
    ]


# packet 0x812
class ZC_FAILED_OPEN_BUYING_STORE_TO_BUYER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('total_weight', ctypes.c_uint32)
	]

class ZC_MYITEMLIST_BUYING_STORE_ITEMLIST(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('price', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
    ]
# packet 0x813
class ZC_MYITEMLIST_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('limitZeny', ctypes.c_uint32),
        ('itemList', ZC_MYITEMLIST_BUYING_STORE_ITEMLIST * 0)
    ]


# packet 0x814
class ZC_BUYING_STORE_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32),
		('storeName', ctypes.c_char * 80)
	]


# packet 0x815
class CZ_REQ_CLOSE_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x816
class ZC_DISAPPEAR_BUYING_STORE_ENTRY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32)
	]


# packet 0x817
class CZ_REQ_CLICK_TO_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32)
	]

class ZC_ACK_ITEMLIST_BUYING_STORE_ITEMLIST(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('price', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('ITID', ctypes.c_uint16),
    ]
# packet 0x818
class ZC_ACK_ITEMLIST_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32),
		('StoreID', ctypes.c_uint32),
		('limitZeny', ctypes.c_uint32),
        ('itemList', ZC_ACK_ITEMLIST_BUYING_STORE_ITEMLIST * 0)
    ]

class CZ_REQ_TRADE_BUYING_STORE_ITEMLIST(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('count', ctypes.c_uint16),
    ]

# packet 0x819
class CZ_REQ_TRADE_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('makerAID', ctypes.c_uint32),
		('StoreID', ctypes.c_uint32),
        ('itemList', CZ_REQ_TRADE_BUYING_STORE_ITEMLIST * 0)
    ]


# packet 0x81a
class ZC_FAILED_TRADE_BUYING_STORE_TO_BUYER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x81b
class ZC_UPDATE_ITEM_FROM_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('limitZeny', ctypes.c_uint32)
	]


# packet 0x81c
class ZC_ITEM_DELETE_BUYING_STORE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('zeny', ctypes.c_uint32)
	]


# packet 0x81d
class ZC_EL_INIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('hp', ctypes.c_uint32),
		('maxHP', ctypes.c_uint32),
		('sp', ctypes.c_uint32),
		('maxSP', ctypes.c_uint32)
	]


# packet 0x81e
class ZC_EL_PAR_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('var', ctypes.c_uint16),
		('value', ctypes.c_uint32)
	]


# packet 0x81f
class ZC_BROADCAST4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PakcetType', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Msgtype', ctypes.c_uint8),
		('ColorRGB', ctypes.c_uint32),
		('msg', ctypes.c_char * 255)
    ]


# packet 0x820
class ZC_COSTUME_SPRITE_CHANGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('value', ctypes.c_uint32)
	]


# packet 0x821
class AC_OTP_USER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x822
class CA_OTP_AUTH_REQ(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('OTPCode', ctypes.c_char * 7)
	]


# packet 0x823
class AC_OTP_AUTH_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('LoginResult', ctypes.c_uint16)
	]


# packet 0x824
class ZC_FAILED_TRADE_BUYING_STORE_TO_SELLER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('ITID', ctypes.c_uint16)
	]


# packet 0x825a
class CA_SSO_LOGIN_REQa(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('clienttype', ctypes.c_uint8),
		('ID', ctypes.c_char * 24),
		('MacAddr', ctypes.c_char * 17),
		('IpAddr', ctypes.c_char * 15),
		('t1', ctypes.c_char * 255)
    ]


# packet 0x825
class CA_SSO_LOGIN_REQ(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('clienttype', ctypes.c_uint8),
		('ID', ctypes.c_char * 24),
		('Passwd', ctypes.c_char * 27),
		('MacAdress', ctypes.c_char * 17),
		('IP', ctypes.c_char * 15),
		('t1', ctypes.c_char * 255)
    ]


# packet 0x826
class AC_SSO_LOGIN_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x827
class CH_DELETE_CHAR3_RESERVED(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x828
class HC_DELETE_CHAR3_RESERVED(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Result', ctypes.c_uint32),
		('DeleteReservedDate', ctypes.c_uint32)
	]


# packet 0x829
class CH_DELETE_CHAR3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Birth', ctypes.c_char * 6)
	]


# packet 0x82a
class HC_DELETE_CHAR3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Result', ctypes.c_uint32)
	]


# packet 0x82b
class CH_DELETE_CHAR3_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x82c
class HC_DELETE_CHAR3_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Result', ctypes.c_uint32)
	]

class HC_ACCEPT2_CHARINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('GID', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('money', ctypes.c_uint32),
		('jobexp', ctypes.c_uint32),
		('joblevel', ctypes.c_uint32),
		('bodystate', ctypes.c_uint32),
		('healthstate', ctypes.c_uint32),
		('effectstate', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('jobpoint', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxhp', ctypes.c_uint32),
		('sp', ctypes.c_uint16),
		('maxsp', ctypes.c_uint16),
		('speed', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('sppoint', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('Str', ctypes.c_uint8),
		('Agi', ctypes.c_uint8),
		('Vit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('Dex', ctypes.c_uint8),
		('Luk', ctypes.c_uint8),
		('CharNum', ctypes.c_uint8),
		('haircolor', ctypes.c_uint8),
		('bIsChangedCharName', ctypes.c_uint16),
		('Robe', ctypes.c_uint32),
    ]
# packet 0x82d
class HC_ACCEPT2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('NormalSlotNum', ctypes.c_uint8),
		('PremiumSlotNum', ctypes.c_uint8),
		('BillingSlotNum', ctypes.c_uint8),
		('ProducibleSlotNum', ctypes.c_uint8),
		('ValidSlotNum', ctypes.c_uint8),
		('m_extension', ctypes.c_char * 20),
		('charList', HC_ACCEPT2_CHARINFO * 0)
    ]


# packet 0x835
class CZ_SEARCH_STORE_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('StoreType', ctypes.c_uint8),
		('maxPrice', ctypes.c_uint32),
		('minPrice', ctypes.c_uint32),
		('ItemIDListSize', ctypes.c_uint8),
		('CardIDListSize', ctypes.c_uint8)
	]

class ZC_SEARCH_STORE_INFO_ACK_LIST(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('SSI_ID', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('StoreName', ctypes.c_char * 80),
		('ITID', ctypes.c_uint16),
		('ItemType', ctypes.c_uint8),
		('price', ctypes.c_uint32),
		('count', ctypes.c_uint16),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
    ]
# packet 0x836
class ZC_SEARCH_STORE_INFO_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('IsFirstPage', ctypes.c_uint8),
		('IsNexPage', ctypes.c_uint8),
		('RemainedSearchCnt', ctypes.c_uint8),
		('SSI_List', ZC_SEARCH_STORE_INFO_ACK_LIST * 0)
    ]


# packet 0x837
class ZC_SEARCH_STORE_INFO_FAILED(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Reason', ctypes.c_uint8)
	]


# packet 0x838
class CZ_SEARCH_STORE_INFO_NEXT_PAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x839
class ZC_ACK_BAN_GUILD_SSO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('charName', ctypes.c_char * 24),
		('reasonDesc', ctypes.c_char * 40)
	]


# packet 0x83a
class ZC_OPEN_SEARCH_STORE_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('OpenType', ctypes.c_uint16),
		('SearchCntMax', ctypes.c_uint8)
	]


# packet 0x83b
class CZ_CLOSE_SEARCH_STORE_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x83c
class CZ_SSILIST_ITEM_CLICK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('SSI_ID', ctypes.c_uint32),
		('ITID', ctypes.c_uint16)
	]


# packet 0x83d
class ZC_SSILIST_ITEM_CLICK_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('x', ctypes.c_uint16),
		('y', ctypes.c_uint16)
	]


# packet 0x83e
class AC_REFUSE_LOGIN_R2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint32),
		('blockDate', ctypes.c_char * 20)
	]


# packet 0x83f
class ZC_SEARCH_STORE_OPEN_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x841
class CH_SELECT_ACCESSIBLE_MAPNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CharNum', ctypes.c_uint8),
		('mapListNum', ctypes.c_uint8)
	]


# packet 0x842
class CZ_RECALL_SSO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('aid', ctypes.c_uint32)
	]


# packet 0x843
class CZ_REMOVE_AID_SSO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('aid', ctypes.c_uint32)
	]


# packet 0x844
class CZ_SE_CASHSHOP_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x845
class ZC_SE_CASHSHOP_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('cash_point', ctypes.c_uint32)
	]


# packet 0x846
class CZ_REQ_SE_CASH_TAB_CODE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('tab_code', ctypes.c_uint16)
	]

class ZC_ACK_SE_CASH_ITEM_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('item_id', ctypes.c_uint32),
		('price', ctypes.c_uint32),
    ]
# packet 0x847
class ZC_ACK_SE_CASH_ITEM_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('item_count', ctypes.c_uint16),
        ('itemList', ZC_ACK_SE_CASH_ITEM_LIST_SUB * 0)
    ]

class CZ_SE_PC_BUY_CASHITEM_LIST_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('item_id', ctypes.c_uint32),
		('count', ctypes.c_uint32),
		('tab_code', ctypes.c_uint16),
    ]
# packet 0x848
class CZ_SE_PC_BUY_CASHITEM_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('item_count', ctypes.c_uint16),
        ('itemList', CZ_SE_PC_BUY_CASHITEM_LIST_SUB * 0)
    ]


# packet 0x849
class ZC_SE_PC_BUY_CASHITEM_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('item_id', ctypes.c_uint32),
		('result', ctypes.c_uint16)
	]


# packet 0x84a
class CZ_SE_CASHSHOP_CLOSE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x84b
class ZC_ITEM_FALL_ENTRY4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('subX', ctypes.c_uint8),
		('subY', ctypes.c_uint8),
		('count', ctypes.c_uint16)
	]


# packet 0x84c
class CZ_MACRO_USE_SKILL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('targetID', ctypes.c_uint32)
	]


# packet 0x84d
class CZ_MACRO_USE_SKILL_TOGROUND(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('selectedLevel', ctypes.c_uint16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x84e
class CZ_MACRO_REQUEST_MOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dest', ctypes.c_char * 3)
	]


# packet 0x84f
class CZ_MACRO_ITEM_PICKUP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32)
	]


# packet 0x850
class CZ_MACRO_REQUEST_ACT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('action', ctypes.c_uint8),
		('targetGID', ctypes.c_uint32)
	]


# packet 0x851
class ZC_GPK_DYNCODE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('code', ctypes.c_char * 255)
    ]


# packet 0x852
class CZ_GPK_DYNCODE_RELOAD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x855
class ZC_MACRO_ITEMPICKUP_FAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITAID', ctypes.c_uint32)
	]


# packet 0x856
class ZC_NOTIFY_MOVEENTRY8(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16)
	]


# packet 0x857
class ZC_NOTIFY_STANDENTRY7(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16)
	]


# packet 0x858
class ZC_NOTIFY_NEWENTRY6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16)
	]


# packet 0x859
class ZC_EQUIPWIN_MICROSCOPE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('sex', ctypes.c_uint8)
	]


# packet 0x8af
class HC_WAITING_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('CurWaitingNum', ctypes.c_uint32)
	]


# packet 0x8b0
class CH_WAITING_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('AuthCode', ctypes.c_uint32),
		('userLevel', ctypes.c_uint32),
		('clientType', ctypes.c_uint16),
		('Sex', ctypes.c_uint8)
	]


# packet 0x8b4
class ZC_START_COLLECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x8b5
class CZ_TRYCOLLECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('targetAID', ctypes.c_uint32)
	]


# packet 0x8b6
class ZC_TRYCOLLECTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x8b7
class HC_SECOND_PASSWD_REQ(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Seed', ctypes.c_uint32)
	]


# packet 0x8b8
class CH_SECOND_PASSWD_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('SecondPWIdx', ctypes.c_char * 6)
	]


# packet 0x8b9
class HC_SECOND_PASSWD_LOGIN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Seed', ctypes.c_uint32),
		('AID', ctypes.c_uint32),
		('Result', ctypes.c_uint16)
	]


# packet 0x8ba
class CH_MAKE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Seed', ctypes.c_uint32),
		('SecondPWIdx', ctypes.c_char * 6)
	]


# packet 0x8bb
class HC_MAKE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x8bc
class CH_DELETE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Seed', ctypes.c_uint32),
		('SecondPWIdx', ctypes.c_char * 6)
	]


# packet 0x8bd
class HC_DELETE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x8be
class CH_EDIT_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Seed', ctypes.c_uint32),
		('SecondPWIdx', ctypes.c_char * 6)
	]


# packet 0x8bf
class HC_EDIT_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]

class ZC_ACK_SE_CASH_ITEM_LIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('item_id', ctypes.c_uint16),
		('price', ctypes.c_uint32),
    ]

# packet 0x8c0
class ZC_ACK_SE_CASH_ITEM_LIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('OpenIdentity', ctypes.c_uint32),
		('item_count', ctypes.c_uint16),
		('item_list', ZC_ACK_SE_CASH_ITEM_LIST2_SUB * 0),
    ]


# packet 0x8c1
class CZ_MACRO_START(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x8c2
class CZ_MACRO_STOP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x8c3
class CH_NOT_AVAILABLE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('SecondPWIdx', ctypes.c_char * 4)
	]


# packet 0x8c4
class HC_NOT_AVAILABLE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('Seed', ctypes.c_uint32)
	]


# packet 0x8c5
class CH_AVAILABLE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x8c6
class HC_AVAILABLE_SECOND_PASSWD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x8c7
class ZC_SKILL_ENTRY3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('creatorAID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('job', ctypes.c_uint8),
		('RadiusRange', ctypes.c_uint8),
		('isVisible', ctypes.c_uint8)
	]


# packet 0x8c8
class ZC_NOTIFY_ACT3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('targetGID', ctypes.c_uint32),
		('startTime', ctypes.c_uint32),
		('attackMT', ctypes.c_uint32),
		('attackedMT', ctypes.c_uint32),
		('damage', ctypes.c_uint32),
		('IsSPDamage', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('action', ctypes.c_uint8),
		('leftDamage', ctypes.c_uint32)
	]


# packet 0x8c9
class CZ_REQ_SCHEDULER_CASHITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]

class ZC_PERSONAL_INFORMATION_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('InfoType', ctypes.c_uint8),
		('Exp', ctypes.c_uint16),
		('Death', ctypes.c_uint16),
		('Drop', ctypes.c_uint16),
    ]

# packet 0x8cb
class ZC_PERSONAL_INFOMATION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Exp', ctypes.c_uint16),
		('Death', ctypes.c_uint16),
		('Drop', ctypes.c_uint16),
		('PersonalInfo', ZC_PERSONAL_INFORMATION_SUB * 0),
    ]


# packet 0x8cc
class CA_LOGIN5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 51),
		('Passwd', ctypes.c_char * 51),
		('clienttype', ctypes.c_uint8)
	]


# packet 0x8cd
class ZC_STOPMOVE_FORCE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x8ce
class ZC_FAILED_GET_ITEM_FROM_ZONEDA(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x8cf
class ZC_SPIRITS_ATTRIBUTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('SpritsType', ctypes.c_uint16),
		('Num', ctypes.c_uint16)
	]


# packet 0x8d0
class ZC_REQ_WEAR_EQUIP_ACK2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x8d1
class ZC_REQ_TAKEOFF_EQUIP_ACK2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x8d2
class ZC_FASTMOVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('targetXpos', ctypes.c_uint16),
		('targetYpos', ctypes.c_uint16)
	]


# packet 0x8d3
class ZC_SE_CASHSHOP_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('cash_point', ctypes.c_uint32),
		('free_point', ctypes.c_uint32)
	]


# packet 0x8d4
class CH_REQ_CHANGE_CHARACTER_SLOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('beforeCharNum', ctypes.c_uint16),
		('AfterCharNum', ctypes.c_uint16),
		('CurChrSlotCnt', ctypes.c_uint16)
	]


# packet 0x8d5
class HC_ACK_CHANGE_CHARACTER_SLOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Reason', ctypes.c_uint16),
		('AfterChrSlotCnt', ctypes.c_uint16)
	]


# packet 0x8d6
class ZC_CLEAR_DIALOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32)
	]


# packet 0x8d7
class CZ_REQ_ENTRY_QUEUE_APPLY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ApplyType', ctypes.c_uint16),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8d8
class ZC_ACK_ENTRY_QUEUE_APPLY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8d9
class ZC_NOTIFY_ENTRY_QUEUE_APPLY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EntryQueueName', ctypes.c_char * 24),
		('Ranking', ctypes.c_uint32)
	]


# packet 0x8da
class CZ_REQ_ENTRY_QUEUE_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8db
class ZC_ACK_ENTRY_QUEUE_CANCEL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8dc
class ZC_NOTIFY_ENTRY_QUEUE_ADMISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8dd
class CZ_REPLY_ENTRY_QUEUE_ADMISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8de
class ZC_REPLY_ACK_ENTRY_QUEUE_ADMISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x8df
class ZC_NOTIFY_LOBBY_ADMISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EntryQueueName', ctypes.c_char * 24),
		('LobbyName', ctypes.c_char * 24)
	]


# packet 0x8e0
class CZ_REPLY_LOBBY_ADMISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('EntryQueueName', ctypes.c_char * 24),
		('LobbyName', ctypes.c_char * 24)
	]


# packet 0x8e1
class ZC_REPLY_ACK_LOBBY_ADMISSION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('EntryQueueName', ctypes.c_char * 24),
		('LobbyName', ctypes.c_char * 24)
	]


# packet 0x8e2
class ZC_NAVIGATION_ACTIVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Type', ctypes.c_uint8),
		('SetType', ctypes.c_uint8),
		('Hide', ctypes.c_uint8),
		('MapName', ctypes.c_char * 16),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('sprIndex', ctypes.c_uint16)
	]

class HC_UPDATE_CHARINFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
	    
		('GID', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('money', ctypes.c_uint32),
		('jobexp', ctypes.c_uint32),
		('joblevel', ctypes.c_uint32),
		('bodystate', ctypes.c_uint32),
		('healthstate', ctypes.c_uint32),
		('effectstate', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('jobpoint', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxhp', ctypes.c_uint32),
		('sp', ctypes.c_uint16),
		('maxsp', ctypes.c_uint16),
		('speed', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('sppoint', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('Str', ctypes.c_uint8),
		('Agi', ctypes.c_uint8),
		('Vit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('Dex', ctypes.c_uint8),
		('Luk', ctypes.c_uint8),
		('CharNum', ctypes.c_uint8),
		('haircolor', ctypes.c_uint8),
		('bIsChangedCharName', ctypes.c_uint16),
		('lastMap', ctypes.c_char * 16),
		('DeleteDate', ctypes.c_uint32),
		('Robe', ctypes.c_uint32),
		('SlotAddon', ctypes.c_uint32),
		('RenameAddon', ctypes.c_uint32),
    ]
    _sizeof_ = 144

# packet 0x8e3
class HC_UPDATE_CHARINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
        ('charInfoList', HC_UPDATE_CHARINFO_SUB * 0)
    ]


# packet 0x8e4
class AC_SHUTDOWN_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Time', ctypes.c_uint32)
	]

class CZ_PARTY_RECRUIT_REQ_REGISTER_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('Level', ctypes.c_uint16),
		('Notice', ctypes.c_char * 37),
    ]
# packet 0x8e5
class CZ_PARTY_RECRUIT_REQ_REGISTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
        ('partyRecruitInfo', CZ_PARTY_RECRUIT_REQ_REGISTER_SUB * 0)
    ]


# packet 0x8e6
class ZC_PARTY_RECRUIT_ACK_REGISTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x8e7
class CZ_PARTY_RECRUIT_REQ_SEARCH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Level', ctypes.c_uint16),
		('LastIndex', ctypes.c_uint32),
		('ResultCount', ctypes.c_uint16)
	]


# packet 0x8e9
class CZ_PARTY_RECRUIT_REQ_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x8ea
class ZC_PARTY_RECRUIT_ACK_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x8eb
class CZ_PARTY_RECRUIT_REQ_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Notice', ctypes.c_char * 37)
	]


# packet 0x8ec
class ZC_PARTY_RECRUIT_NOTIFY_INSERT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32),
		('ExpireTime', ctypes.c_uint32),
		('CharName', ctypes.c_char * 24),
		('Level', ctypes.c_uint16),
		('Notice', ctypes.c_char * 37)
	]


# packet 0x8ed
class ZC_PARTY_RECRUIT_NOTIFY_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32),
		('Notice', ctypes.c_char * 37)
	]


# packet 0x8ee
class ZC_PARTY_RECRUIT_NOTIFY_DELETE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x8ef
class CZ_PARTY_RECRUIT_ADD_FILTERLINGLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x8f0
class CZ_PARTY_RECRUIT_SUB_FILTERLINGLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0x8f1
class CZ_PARTY_RECRUIT_REQ_VOLUNTEER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x8f2
class ZC_PARTY_RECRUIT_VOLUNTEER_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Job', ctypes.c_uint32),
		('Level', ctypes.c_uint16),
		('CharName', ctypes.c_char * 24)
	]


# packet 0x8f4
class CZ_PARTY_RECRUIT_SHOW_EQUIPMENT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('TargetGID', ctypes.c_uint32)
	]


# packet 0x8f6
class ZC_PARTY_RECRUIT_RECALL_COST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Money', ctypes.c_uint32),
		('mapName', ctypes.c_char * 16)
	]


# packet 0x8f7
class CZ_PARTY_RECRUIT_ACK_RECALL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x8f8
class ZC_PARTY_RECRUIT_FAILED_RECALL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('CallerAID', ctypes.c_uint32),
		('Reason', ctypes.c_uint8)
	]


# packet 0x8f9
class CZ_PARTY_RECRUIT_REFUSE_VOLUNTEER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('REFUSE_AID', ctypes.c_uint32)
	]


# packet 0x8fa
class ZC_PARTY_RECRUIT_REFUSE_VOLUNTEER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x8fb
class CZ_PARTY_RECRUIT_CANCEL_VOLUNTEER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint32)
	]


# packet 0x8fc
class CH_REQ_CHANGE_CHARACTERNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dwGID', ctypes.c_uint32),
		('szCharName', ctypes.c_char * 24)
	]


# packet 0x8fd
class HC_ACK_CHANGE_CHARACTERNAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('dwResult', ctypes.c_uint32)
	]


# packet 0x8ff
class ZC_EFST_SET_ENTER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('hEFST', ctypes.c_uint16),
		('Time', ctypes.c_uint32),
		('Val1', ctypes.c_uint32),
		('Val2', ctypes.c_uint32),
		('Val3', ctypes.c_uint32)
	]

class ZC_INVENTORY_ITEMLIST_NORMAL_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x900
class ZC_INVENTORY_ITEMLIST_NORMAL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_INVENTORY_ITEMLIST_NORMAL_SUB * 0),
    ]


class ZC_INVENTORY_ITEMLIST_EQUIP_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('location', ctypes.c_uint16),
		('WearState', ctypes.c_uint16),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x901
class ZC_INVENTORY_ITEMLIST_EQUIP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_INVENTORY_ITEMLIST_EQUIP_SUB * 0),
    ]


# packet 0x907
class CZ_INVENTORY_TAB(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('NORMALorPRIVATE', ctypes.c_uint8)
	]


# packet 0x908
class ZC_INVENTORY_TAB(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('NORMALorPRIVATE', ctypes.c_uint8)
	]


# packet 0x909
class ZC_PARTY_RECRUIT_CANCEL_VOLUNTEER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint32)
	]


# packet 0x90a
class CZ_REQ_ENTRY_QUEUE_RANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('EntryQueueName', ctypes.c_char * 24)
	]


# packet 0x90b
class ZC_PARTY_RECRUIT_ADD_FILTERLINGLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('CharName', ctypes.c_char * 24)
	]


# packet 0x90c
class ZC_PARTY_RECRUIT_SUB_FILTERLINGLIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('CharName', ctypes.c_char * 24)
	]

class ZC_PREMIUM_CAMPAIGN_INFO_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('Grade', ctypes.c_uint16),
		('Exp', ctypes.c_uint32),
		('Death', ctypes.c_uint32),
		('Drp', ctypes.c_uint32),
    ]
# packet 0x90d
class ZC_PREMIUM_CAMPAIGN_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Count', ctypes.c_uint16),
		('PremiumValue', ctypes.c_uint32),
        ('campaignInfo', ZC_PREMIUM_CAMPAIGN_INFO_SUB * 0),
    ]


# packet 0x90e
class ZC_ENTRY_QUEUE_INIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x90f
class ZC_NOTIFY_NEWENTRY7(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8)
	]


# packet 0x910
class CZ_REQ_PARTY_NAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('PartyID', ctypes.c_uint32)
	]


# packet 0x911
class ZC_ACK_PARTY_NAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PartyID', ctypes.c_uint32),
		('szPartyName', ctypes.c_char * 24)
	]


# packet 0x912
class CZ_REQ_GUILD_NAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('GuildID', ctypes.c_uint32)
	]


# packet 0x914
class ZC_NOTIFY_MOVEENTRY9(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8)
	]


# packet 0x915
class ZC_NOTIFY_STANDENTRY8(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8)
	]


# packet 0x916
class CZ_REQ_JOIN_GUILD2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24)
	]


# packet 0x91b
class ZC_PRNPC_STATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Winner', ctypes.c_uint8),
		('Point', ctypes.c_uint8)
	]


# packet 0x91c
class ZC_PARTY_RECRUIT_CANCEL_VOLUNTEER_TO_PM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x96f
class ZC_ACK_MERGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('item_index', ctypes.c_uint16),
		('item_count', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0x970
class CH_MAKE_CHAR_NOT_STATS(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('CharNum', ctypes.c_uint8),
		('headPal', ctypes.c_uint16),
		('head', ctypes.c_uint16)
	]


# packet 0x971
class ZC_PARTY_RECRUIT_REFUSE_VOLUNTEER_TO_PM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PM_AID', ctypes.c_uint32)
	]


# packet 0x973
class ZC_WAIT_DIALOG2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NAID', ctypes.c_uint32),
		('type', ctypes.c_uint8)
	]


# packet 0x974
class CZ_CANCEL_MERGE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x977
class ZC_HP_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('MaxHP', ctypes.c_uint32)
	]


# packet 0x978
class CZ_REQ_BEFORE_WORLD_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x979
class ZC_ACK_BEFORE_WORLD_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('WorldName', ctypes.c_char * 24),
		('CharName', ctypes.c_char * 24)
	]

class ZC_ALL_QUEST_LIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8),
		('quest_svrTime', ctypes.c_uint32),
		('quest_endTime', ctypes.c_uint32),
		('hunting_count', ctypes.c_uint16),
    ]
# packet 0x97a
class ZC_ALL_QUEST_LIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('QuestCount', ctypes.c_uint32),
		('questList', ZC_ALL_QUEST_LIST2_SUB * 1)
    ]

class ZC_PERSONAL_INFORMATION2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('InfoType', ctypes.c_uint8),
		('Exp', ctypes.c_uint32),
		('Death', ctypes.c_uint32),
		('Drop', ctypes.c_uint32)
    ]
# packet 0x97b
class ZC_PERSONAL_INFOMATION2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Exp', ctypes.c_uint32),
		('Death', ctypes.c_uint32),
		('Drop', ctypes.c_uint32),
        ('infoList', ZC_PERSONAL_INFORMATION2_SUB * 1)
    ]


# packet 0x97c
class CZ_REQ_RANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('RankingType', ctypes.c_uint16)
	]


# packet 0x97d
class ZC_ACK_RANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('RankingType', ctypes.c_uint16),
		('CharName', ctypes.c_char * 24),
		('Point', ctypes.c_uint32),
		('myPoint', ctypes.c_uint32)
	]


# packet 0x97e
class ZC_UPDATE_RANKING_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('RankingType', ctypes.c_uint16),
		('Point', ctypes.c_uint32),
		('TotalPoint', ctypes.c_uint32)
	]


# packet 0x980
class CZ_SELECTCART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Identity', ctypes.c_uint32),
		('type', ctypes.c_uint8)
	]

class ZC_PERSONAL_INFORMATION_CHN_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('InfoType', ctypes.c_uint8),
		('Exp', ctypes.c_uint32),
		('Death', ctypes.c_uint32),
		('Drop', ctypes.c_uint32),
    ]
# packet 0x981
class ZC_PERSONAL_INFOMATION_CHN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Exp', ctypes.c_uint16),
		('Death', ctypes.c_uint16),
		('Drop', ctypes.c_uint16),
		('ActivityRate', ctypes.c_uint16),
        ('infoList', ZC_PERSONAL_INFORMATION_CHN_SUB * 1)
    ]


# packet 0x982
class ZC_FATIGUE_CHN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Level', ctypes.c_uint8),
		('TotalPlayTime', ctypes.c_uint32)
	]


# packet 0x983
class ZC_MSG_STATE_CHANGE3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('state', ctypes.c_uint8),
		('MaxMS', ctypes.c_uint32),
		('RemainMS', ctypes.c_uint32),
		('val', ctypes.c_uint32)
	]


# packet 0x984
class ZC_EFST_SET_ENTER2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('hEFST', ctypes.c_uint16),
		('MaxMS', ctypes.c_uint32),
		('Time', ctypes.c_uint32),
		('Val1', ctypes.c_uint32),
		('Val2', ctypes.c_uint32),
		('Val3', ctypes.c_uint32)
	]

class ZC_SKILL_POSTDELAY_LIST2_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('SKID', ctypes.c_uint16),
		('MaxDelayTM', ctypes.c_uint32),
		('DelayTM', ctypes.c_uint32),
    ]
# packet 0x985
class ZC_SKILL_POSTDELAY_LIST2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('skillList', ZC_SKILL_POSTDELAY_LIST2_SUB * 1)
    ]


# packet 0x986
class AC_SHUTDOWN_NOTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Time', ctypes.c_uint32),
		('ServerTime', ctypes.c_uint32)
	]


# packet 0x987
class CA_LOGIN6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('ID', ctypes.c_char * 24),
		('PasswdMD5', ctypes.c_char * 32),
		('clienttype', ctypes.c_uint8)
	]


# packet 0x988
class ZC_NOTIFY_CLAN_CONNECTINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NumConnect', ctypes.c_uint16),
		('NumTotal', ctypes.c_uint16)
	]


# packet 0x989
class ZC_ACK_CLAN_LEAVE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x98a
class ZC_CLANINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('EmblemNum', ctypes.c_uint32),
		('ClanName', ctypes.c_char * 24),
		('Mastername', ctypes.c_char * 24),
		('ManageMap', ctypes.c_char * 16),
		('Num_AllyClan', ctypes.c_uint8),
		('Num_HostileClan', ctypes.c_uint8)
	]


# packet 0x98b
class AC_REQ_NEW_USER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x98c
class CA_ACK_NEW_USER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Sex', ctypes.c_uint16)
	]


# packet 0x98d
class CZ_CLAN_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('chat', ctypes.c_char * 255)
    ]


# packet 0x98e
class ZC_NOTIFY_CLAN_CHAT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('charName', ctypes.c_char * 24),
		('chat', ctypes.c_char * 255)
    ]


# packet 0x990
class ZC_ITEM_PICKUP_ACK_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('location', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16)
	]

class ZC_INVENTORY_ITEMLIST_NORMAL_v5_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint32),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('Flag', ctypes.c_uint8)
    ]
# packet 0x991
class ZC_INVENTORY_ITEMLIST_NORMAL_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('Items', ZC_INVENTORY_ITEMLIST_NORMAL_v5_ITEMINFO * 1)
    ]

class ZC_INVENTORY_ITEMLIST_EQUIP_V5_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('location', ctypes.c_uint32),
		('WearState', ctypes.c_uint32),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x992
class ZC_INVENTORY_ITEMLIST_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('Items', ZC_INVENTORY_ITEMLIST_EQUIP_V5_ITEMINFO * 1)
    ]
	

class ZC_CART_ITEMLIST_NORMAL_V5_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint32),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x993
class ZC_CART_ITEMLIST_NORMAL_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_CART_ITEMLIST_NORMAL_V5_ITEMINFO * 1)
    ]

class ZC_CART_ITEMLIST_EQUIP_V5_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
	    
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('location', ctypes.c_uint32),
		('WearState', ctypes.c_uint32),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x994
class ZC_CART_ITEMLIST_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_CART_ITEMLIST_EQUIP_V5_ITEMINFO * 1)
    ]


class ZC_STORE_ITEMLIST_NORMAL_V5_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('count', ctypes.c_uint16),
		('WearState', ctypes.c_uint32),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x995
class ZC_STORE_ITEMLIST_NORMAL_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_STORE_ITEMLIST_NORMAL_V5_ITEMINFO * 1)
    ]

class ZC_STORE_ITEMLIST_EQUIP_V5_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('location', ctypes.c_uint32),
		('WearState', ctypes.c_uint32),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('Flag', ctypes.c_uint8),
    ]
# packet 0x996
class ZC_STORE_ITEMLIST_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('itemList', ZC_STORE_ITEMLIST_EQUIP_V5_ITEMINFO * 1)
    ]


# packet 0x997
class ZC_EQUIPWIN_MICROSCOPE_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Length', ctypes.c_uint16),
		('characterName', ctypes.c_char * 24),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('sex', ctypes.c_uint8)
	]


# packet 0x998
class CZ_REQ_WEAR_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint32)
	]


# packet 0x999
class ZC_ACK_WEAR_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint32),
		('wItemSpriteNumber', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x99a
class ZC_ACK_TAKEOFF_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('wearLocation', ctypes.c_uint32),
		('result', ctypes.c_uint8)
	]


# packet 0x99b
class ZC_MAPPROPERTY_R2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('type', ctypes.c_uint16),
		('NotifyPropertyBits', ctypes.c_uint32)
	]


# packet 0x99c
class CH_REQ_CHARINFO_PER_PAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SeqNum', ctypes.c_uint32)
	]


class HC_ACK_CHARINFO_PER_PAGE_CHARINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('GID', ctypes.c_uint32),
		('exp', ctypes.c_uint32),
		('money', ctypes.c_uint32),
		('jobexp', ctypes.c_uint32),
		('joblevel', ctypes.c_uint32),
		('bodystate', ctypes.c_uint32),
		('healthstate', ctypes.c_uint32),
		('effectstate', ctypes.c_uint32),
		('virtue', ctypes.c_uint32),
		('honor', ctypes.c_uint32),
		('jobpoint', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxhp', ctypes.c_uint32),
		('sp', ctypes.c_uint16),
		('maxsp', ctypes.c_uint16),
		('speed', ctypes.c_uint16),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint16),
		('level', ctypes.c_uint16),
		('sppoint', ctypes.c_uint16),
		('accessory', ctypes.c_uint16),
		('shield', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('name', ctypes.c_char * 24),
		('Str', ctypes.c_uint8),
		('Agi', ctypes.c_uint8),
		('Vit', ctypes.c_uint8),
		('Int', ctypes.c_uint8),
		('Dex', ctypes.c_uint8),
		('Luk', ctypes.c_uint8),
		('CharNum', ctypes.c_uint8),
		('haircolor', ctypes.c_uint8),
		('bIsChangedCharName', ctypes.c_uint16),
		('lastMap', ctypes.c_char * 16),
		('DeleteDate', ctypes.c_uint32),
		('Robe', ctypes.c_uint32),
		('SlotAddon', ctypes.c_uint32),
		('RenameAddon', ctypes.c_uint32),
    ]
# packet 0x99d
class HC_ACK_CHARINFO_PER_PAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('CharInfo', HC_ACK_CHARINFO_PER_PAGE_CHARINFO * 0)
    ]

# packet 0x99e
class HC_QUEUE_ORDER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('m_AID', ctypes.c_uint32),
		('m_QueueOrder', ctypes.c_uint32)
	]


# packet 0x99f
class ZC_SKILL_ENTRY4(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('creatorAID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('job', ctypes.c_uint32),
		('RadiusRange', ctypes.c_uint8),
		('isVisible', ctypes.c_uint8)
	]


# packet 0x9a0
class HC_CHARLIST_NOTIFY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('TotalCnt', ctypes.c_uint32)
	]


# packet 0x9a1
class CH_CHARLIST_REQ(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9a2
class AC_REQ_MOBILE_OTP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9a4
class ZC_DISPATCH_TIMING_INFO_CHN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Balance', ctypes.c_uint32),
		('Effective_dTime', ctypes.c_uint32),
		('Reason', ctypes.c_uint32)
	]


# packet 0x9a5
class AC_REFUSE_LOGIN3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCode', ctypes.c_uint8),
		('BlockedReaminSEC', ctypes.c_uint32)
	]


# packet 0x9a6
class ZC_BANKING_CHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
	    ('Money', ctypes.c_uint64),
		('Reason', ctypes.c_uint16)
	]


# packet 0x9a7
class CZ_REQ_BANKING_DEPOSIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Money', ctypes.c_uint32)
	]


# packet 0x9a8
class ZC_ACK_BANKING_DEPOSIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Reason', ctypes.c_uint16),
	    ('Money', ctypes.c_uint64),
    ]


# packet 0x9a9
class CZ_REQ_BANKING_WITHDRAW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('Money', ctypes.c_uint32)
	]


# packet 0x9aa
class ZC_ACK_BANKING_WITHDRAW(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Reason', ctypes.c_uint16),
	    ('Money', ctypes.c_uint64),
    ]


# packet 0x9ab
class CZ_REQ_BANKING_CHECK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9ac
class CZ_REQ_CASH_BARGAIN_SALE_ITEM_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9ad
class ZC_ACK_CASH_BARGAIN_SALE_ITEM_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('ItemID', ctypes.c_uint16),
		('Price', ctypes.c_uint32)
	]


# packet 0x9ae
class CZ_REQ_APPLY_BARGAIN_SALE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('ItemID', ctypes.c_uint16),
		('Count', ctypes.c_uint32),
		('StartDate', ctypes.c_uint32),
		('SellingTime', ctypes.c_uint8)
	]


# packet 0x9af
class ZC_ACK_APPLY_BARGAIN_SALE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x9b0
class CZ_REQ_REMOVE_BARGAIN_SALE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('ItemID', ctypes.c_uint16)
	]


# packet 0x9b1
class ZC_ACK_REMOVE_BARGAIN_SALE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x9b2
class ZC_NOTIFY_BARGAIN_SALE_SELLING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ItemID', ctypes.c_uint16),
		('TabCode', ctypes.c_uint16)
	]


# packet 0x9b3
class ZC_NOTIFY_BARGAIN_SALE_CLOSE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ItemID', ctypes.c_uint16),
		('TabCode', ctypes.c_uint16)
	]


# packet 0x9b4
class CZ_OPEN_BARGAIN_SALE_TOOL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9b5
class ZC_OPEN_BARGAIN_SALE_TOOL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9b6
class CZ_REQ_OPEN_BANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9b7
class ZC_ACK_OPEN_BANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x9b8
class CZ_REQ_CLOSE_BANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9b9
class ZC_ACK_CLOSE_BANKING(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x9ba
class CZ_REQ_OPEN_GUILD_STORAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9bb
class ZC_ACK_OPEN_GUILD_STORAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('Permission', ctypes.c_uint16)
	]


# packet 0x9bc
class CZ_CLOSE_BARGAIN_SALE_TOOL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32)
	]


# packet 0x9bd
class ZC_CLOSE_BARGAIN_SALE_TOOL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9be
class CZ_REQ_CLOSE_GUILD_STORAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9bf
class ZC_ACK_CLOSE_GUILD_STORAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x9c1
class ZC_C_MARKERINFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16)
	]


# packet 0x9c2
class HC_SECRETSCAN_DATA(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9c3
class CZ_REQ_COUNT_BARGAIN_SALE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('ItemID', ctypes.c_uint16)
	]


# packet 0x9c4
class ZC_ACK_COUNT_BARGAIN_SALE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ItemID', ctypes.c_uint16),
		('RemainCount', ctypes.c_uint32)
	]


# packet 0x9c5
class CS_LOGIN_QUERY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('i64SteamID', ctypes.c_uint64),
		('ticketLength', ctypes.c_uint32),
		('AuthTicket', ctypes.c_char * 1024)
	]


# packet 0x9c6
class SC_LOGIN_ANSWER(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('SteamProcessTM', ctypes.c_uint16),
		('IRWebProcessTM', ctypes.c_uint16),
		('AccDBProcessTM', ctypes.c_uint16),
		('SessionProcessTM', ctypes.c_uint16),
		('TransactionID', ctypes.c_uint32)
	]


# packet 0x9c7
class SC_LOGIN_ERROR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ErrorCategory', ctypes.c_uint32),
		('ErrorCode', ctypes.c_uint32),
		('SteamProcessTM', ctypes.c_uint16),
		('IRWebProcessTM', ctypes.c_uint16),
		('AccDBProcessTM', ctypes.c_uint16),
		('SessionProcessTM', ctypes.c_uint16)
	]


# packet 0x9c8
class CA_LOGIN_OTP(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Version', ctypes.c_uint32),
		('clienttype', ctypes.c_uint8),
		('TransactionID', ctypes.c_uint32)
	]


# packet 0x9c9
class SC_SOCT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9ca
class ZC_SKILL_ENTRY5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('creatorAID', ctypes.c_uint32),
		('xPos', ctypes.c_uint16),
		('yPos', ctypes.c_uint16),
		('job', ctypes.c_uint32),
		('RadiusRange', ctypes.c_uint8),
		('isVisible', ctypes.c_uint8),
		('level', ctypes.c_uint8)
	]


# packet 0x9cb
class ZC_USE_SKILL2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('SKID', ctypes.c_uint16),
		('level', ctypes.c_uint32),
		('targetAID', ctypes.c_uint32),
		('srcAID', ctypes.c_uint32),
		('result', ctypes.c_uint8)
	]


# packet 0x9cc
class ZC_SECRETSCAN_DATA(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9cd
class ZC_MSG_COLOR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('msg', ctypes.c_uint16),
		('color', ctypes.c_uint32)
	]


# packet 0x9ce
class CZ_ITEM_CREATE_EX(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('itemName', ctypes.c_char * 100)
	]


# packet 0x9cf
class ZC_NPROTECTGAMEGUARDCSAUTH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9d0
class CZ_NPROTECTGAMEGUARDCSAUTH(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9d1
class ZC_PROGRESS_ACTOR(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('color', ctypes.c_uint32),
		('time', ctypes.c_uint32)
	]


# packet 0x9d2
class ZC_GUILDSTORAGE_ITEMLIST_NORMAL_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('StoreName', ctypes.c_char * 24)
	]


# packet 0x9d3
class ZC_GUILDSTORAGE_ITEMLIST_EQUIP_V5(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('StoreName', ctypes.c_char * 24)
	]


# packet 0x9d4
class CZ_NPC_TRADE_QUIT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketTpye', ctypes.c_uint16)
	]


# packet 0x9d5
class ZC_NPC_MARKET_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9d6
class CZ_NPC_MARKET_PURCHASE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16)
	]


# packet 0x9d7
class ZC_NPC_MARKET_PURCHASE_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('IsBuyAllItems', ctypes.c_uint8)
	]


# packet 0x9d8
class CZ_NPC_MARKET_CLOSE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9d9
class CZ_REQ_GUILDSTORAGE_LOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('RecentIdx', ctypes.c_uint16)
	]


# packet 0x9da
class ZC_ACK_GUILDSTORAGE_LOG(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('Result', ctypes.c_uint16),
		('Cnt', ctypes.c_uint16)
	]


# packet 0x9db
class ZC_NOTIFY_MOVEENTRY10(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8)
	]


# packet 0x9dc
class ZC_NOTIFY_NEWENTRY10(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8)
	]


# packet 0x9dd
class ZC_NOTIFY_STANDENTRY10(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8)
	]


# packet 0x9de
class ZC_WHISPER02(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('senderGID', ctypes.c_uint32),
		('sender', ctypes.c_char * 24),
		('isAdmin', ctypes.c_uint8)
	]


# packet 0x9df
class ZC_ACK_WHISPER02(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8),
		('ReceiverGID', ctypes.c_uint32)
	]


# packet 0x9e0
class SC_LOGIN_ANSWER_WITH_ID(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('SteamProcessTM', ctypes.c_uint16),
		('IRWebProcessTM', ctypes.c_uint16),
		('AccDBProcessTM', ctypes.c_uint16),
		('SessionProcessTM', ctypes.c_uint16),
		('TransactionID', ctypes.c_uint32),
		('ID', ctypes.c_char * 24)
	]


# packet 0x9e1
class CZ_MOVE_ITEM_FROM_BODY_TO_GUILDSTORAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x9e2
class CZ_MOVE_ITEM_FROM_GUILDSTORAGE_TO_BODY(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x9e3
class CZ_MOVE_ITEM_FROM_CART_TO_GUILDSTORAGE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x9e4
class CZ_MOVE_ITEM_FROM_GUILDSTORAGE_TO_CART(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32)
	]


# packet 0x9e5
class ZC_DELETEITEM_FROM_MCSTORE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ToGID', ctypes.c_uint32),
		('Date', ctypes.c_uint32),
		('Zeny', ctypes.c_uint32)
	]


# packet 0x9e6
class ZC_UPDATE_ITEM_FROM_BUYING_STORE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('Zeny', ctypes.c_uint32),
		('limitZeny', ctypes.c_uint32),
		('FromGID', ctypes.c_uint32),
		('Date', ctypes.c_uint32)
	]


# packet 0x9e7
class ZC_NOTIFY_UNREADMAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x9e8
class CZ_OPEN_MAILBOX(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
		('Upper_MailID', ctypes.c_uint64)
    ]


# packet 0x9e9
class CZ_CLOSE_MAILBOX(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0x9ea
class CZ_REQ_READ_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
		('MailID', ctypes.c_uint64)
    ]


# packet 0x9eb
class ZC_ACK_READ_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
		('MailID', ctypes.c_uint64),
		('TextcontentsLength', ctypes.c_uint16),
		('zeny', ctypes.c_uint64),
		('ItemCnt', ctypes.c_uint8)
	]


# packet 0x9ec
class CZ_REQ_WRITE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('receiveName', ctypes.c_char * 24),
		('senderName', ctypes.c_char * 24),
		('zeny', ctypes.c_uint64),
		('Titlelength', ctypes.c_uint16),
		('TextcontentsLength', ctypes.c_uint16)
	]


# packet 0x9ed
class ZC_ACK_WRITE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8)
	]


# packet 0x9ee
class CZ_REQ_NEXT_MAIL_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
		('Lower_MailID', ctypes.c_uint64),
    ]


# packet 0x9ef
class CZ_REQ_REFRESH_MAIL_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
	    ('Upper_MailID', ctypes.c_uint64),
    ]


# packet 0x9f0
class ZC_ACK_MAIL_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
		('cnt', ctypes.c_uint8),
		('IsEnd', ctypes.c_uint8)
	]


# packet 0x9f1
class CZ_REQ_ZENY_FROM_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
	    ('MailID', ctypes.c_uint64),
		('opentype', ctypes.c_uint8)
	]


# packet 0x9f2
class ZC_ACK_ZENY_FROM_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
    	('MailID', ctypes.c_uint64),
		('opentype', ctypes.c_uint8),
		('result', ctypes.c_uint8)
	]


# packet 0x9f3
class CZ_REQ_ITEM_FROM_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
    	('MailID', ctypes.c_uint64),
		('opentype', ctypes.c_uint8)
	]


# packet 0x9f4
class ZC_ACK_ITEM_FROM_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
    	('MailID', ctypes.c_uint64),
		('opentype', ctypes.c_uint8),
		('result', ctypes.c_uint8)
	]


# packet 0x9f5
class CZ_REQ_DELETE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
	    ('MailID', ctypes.c_uint64),
    ]


# packet 0x9f6
class ZC_ACK_DELETE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('opentype', ctypes.c_uint8),
	    ('MailID', ctypes.c_uint64),
    ]


# packet 0x9f7
class ZC_PROPERTY_HOMUN_2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('szName', ctypes.c_char * 24),
		('bModified', ctypes.c_uint8),
		('nLevel', ctypes.c_uint16),
		('nFullness', ctypes.c_uint16),
		('nRelationship', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('atk', ctypes.c_uint16),
		('Matk', ctypes.c_uint16),
		('hit', ctypes.c_uint16),
		('critical', ctypes.c_uint16),
		('_def', ctypes.c_uint16),
		('Mdef', ctypes.c_uint16),
		('flee', ctypes.c_uint16),
		('aspd', ctypes.c_uint16),
		('hp', ctypes.c_uint32),
		('maxHP', ctypes.c_uint32),
		('sp', ctypes.c_uint16),
		('maxSP', ctypes.c_uint16),
		('exp', ctypes.c_uint32),
		('maxEXP', ctypes.c_uint32),
		('SKPoint', ctypes.c_uint16),
		('ATKRange', ctypes.c_uint16)
	]

class ZC_ALL_QUEST_LIST3_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8),
		('quest_svrTime', ctypes.c_uint32),
		('quest_endTime', ctypes.c_uint32),
		('hunting_count', ctypes.c_uint16),
    ]
# packet 0x9f8
class ZC_ALL_QUEST_LIST3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('QuestCount', ctypes.c_uint32),
        ('QuestList', ZC_ALL_QUEST_LIST3_SUB * 0)
    ]

class ZC_ADD_QUEST_EX_SUB(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('mobGID', ctypes.c_uint32),
		('huntCount', ctypes.c_uint16),
		('mobName', ctypes.c_char * 24),
    ]

# packet 0x9f9
class ZC_ADD_QUEST_EX(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('questID', ctypes.c_uint32),
		('active', ctypes.c_uint8),
		('quest_svrTime', ctypes.c_uint32),
		('quest_endTime', ctypes.c_uint32),
		('count', ctypes.c_uint16),
        ('QuestList', ZC_ADD_QUEST_EX_SUB * 0)
    ]


# packet 0x9fa
class ZC_UPDATE_MISSION_HUNT_EX(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0x9fb
class CZ_PET_EVOLUTION(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('EvolutionPetEggITID', ctypes.c_uint16)
	]


# packet 0x9fc
class ZC_PET_EVOLUTION_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint16)
	]


# packet 0x9fd
class ZC_NOTIFY_MOVEENTRY11(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('moveStartTime', ctypes.c_uint32),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('MoveData', ctypes.c_char * 6),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8),
		('body', ctypes.c_uint16)
	]


# packet 0x9fe
class ZC_NOTIFY_NEWENTRY11(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8),
		('body', ctypes.c_uint16)
	]


# packet 0x9ff
class ZC_NOTIFY_STANDENTRY11(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('objecttype', ctypes.c_uint8),
		('AID', ctypes.c_uint32),
		('GID', ctypes.c_uint32),
		('speed', ctypes.c_uint16),
		('bodyState', ctypes.c_uint16),
		('healthState', ctypes.c_uint16),
		('effectState', ctypes.c_uint32),
		('job', ctypes.c_uint16),
		('head', ctypes.c_uint16),
		('weapon', ctypes.c_uint32),
		('accessory', ctypes.c_uint16),
		('accessory2', ctypes.c_uint16),
		('accessory3', ctypes.c_uint16),
		('headpalette', ctypes.c_uint16),
		('bodypalette', ctypes.c_uint16),
		('headDir', ctypes.c_uint16),
		('robe', ctypes.c_uint16),
		('GUID', ctypes.c_uint32),
		('GEmblemVer', ctypes.c_uint16),
		('honor', ctypes.c_uint16),
		('virtue', ctypes.c_uint32),
		('isPKModeON', ctypes.c_uint8),
		('sex', ctypes.c_uint8),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('state', ctypes.c_uint8),
		('clevel', ctypes.c_uint16),
		('font', ctypes.c_uint16),
		('maxHP', ctypes.c_uint32),
		('HP', ctypes.c_uint32),
		('isBoss', ctypes.c_uint8),
		('body', ctypes.c_uint16)
	]

class ZC_SHORTCUT_KEY_LIST_V3_KEYS(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('isSkill', ctypes.c_uint8),
		('ID', ctypes.c_uint32),
		('count', ctypes.c_uint16),
    ]
# packet 0xa00
class ZC_SHORTCUT_KEY_LIST_V3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Rotate', ctypes.c_uint8),
		('keys', ZC_SHORTCUT_KEY_LIST_V3_KEYS * 0)
    ]

# packet 0xa01
class CZ_SHORTCUTKEYBAR_ROTATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Rotate', ctypes.c_uint8)
	]


# packet 0xa02
class ZC_DRESSROOM_OPEN(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('m_ViewType', ctypes.c_uint16)
	]


# packet 0xa03
class CZ_REQ_CANCEL_WRITE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xa04
class CZ_REQ_ADD_ITEM_TO_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16)
	]


# packet 0xa05
class ZC_ACK_ADD_ITEM_TO_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
        ('PacketType', ctypes.c_uint16),
        ("result", ctypes.c_uint8),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8),
		('weight', ctypes.c_uint16)
	]


# packet 0xa06
class CZ_REQ_REMOVE_ITEM_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('cnt', ctypes.c_uint16)
	]


# packet 0xa07
class ZC_ACK_REMOVE_ITEM_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8),
		('index', ctypes.c_uint16),
		('cnt', ctypes.c_uint16),
		('weight', ctypes.c_uint16)
	]


# packet 0xa08
class CZ_REQ_OPEN_WRITE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('receiveName', ctypes.c_char * 24)
	]


# packet 0xa09
class ZC_ADD_EXCHANGE_ITEM3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('count', ctypes.c_uint32),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8)
	]


# packet 0xa0a
class ZC_ADD_ITEM_TO_STORE3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8)
	]


# packet 0xa0b
class ZC_ADD_ITEM_TO_CART3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('index', ctypes.c_uint16),
		('count', ctypes.c_uint32),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8)
	]


# packet 0xa0c
class ZC_ITEM_PICKUP_ACK_V6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Index', ctypes.c_uint16),
		('count', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('IsIdentified', ctypes.c_uint8),
		('IsDamaged', ctypes.c_uint8),
		('refiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('location', ctypes.c_uint32),
		('type', ctypes.c_uint8),
		('result', ctypes.c_uint8),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8)
	]

class ZC_INVENTORY_ITEMLIST_EQUIP_V6_ITEMINFO(ctypes.Structure):
    _pack_ = 1  
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('location', ctypes.c_uint32),
		('WearState', ctypes.c_uint32),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('nRandomOptionCnt', ctypes.c_uint8),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8),
		('Flag', ctypes.c_uint8),
    ]
# packet 0xa0d
class ZC_INVENTORY_ITEMLIST_EQUIP_V6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('Items', ZC_INVENTORY_ITEMLIST_EQUIP_V6_ITEMINFO * 0)
    ]


# packet 0xa0e
class ZC_BATTLEFIELD_NOTIFY_HP2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('AID', ctypes.c_uint32),
		('hp', ctypes.c_uint32),
		('maxHp', ctypes.c_uint32)
	]

class ZC_CART_ITEMLIST_EQUIP_V6_ITEMINFO(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
		('index', ctypes.c_uint16),
		('ITID', ctypes.c_uint16),
		('type', ctypes.c_uint8),
		('location', ctypes.c_uint32),
		('WearState', ctypes.c_uint32),
		('RefiningLevel', ctypes.c_uint8),
		('card1', ctypes.c_uint16),
		('card2', ctypes.c_uint16),
		('card3', ctypes.c_uint16),
		('card4', ctypes.c_uint16),
		('HireExpireDate', ctypes.c_uint32),
		('bindOnEquipType', ctypes.c_uint16),
		('wItemSpriteNumber', ctypes.c_uint16),
		('nRandomOptionCnt', ctypes.c_uint8),
		('OptIndex', ctypes.c_uint16),
		('Value', ctypes.c_uint16),
		('Parm1', ctypes.c_uint8),
		('Flag', ctypes.c_uint8),
    ]
# packet 0xa0f
class ZC_CART_ITEMLIST_EQUIP_V6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
        ('Items', ZC_CART_ITEMLIST_EQUIP_V6_ITEMINFO * 0)
    ]


# packet 0xa10
class ZC_STORE_ITEMLIST_EQUIP_V6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('StoreName', ctypes.c_char * 24)
	]


# packet 0xa11
class ZC_GUILDSTORAGE_ITEMLIST_EQUIP_V6(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('StoreName', ctypes.c_char * 24)
	]


# packet 0xa12
class ZC_ACK_OPEN_WRITE_MAIL(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('receiveName', ctypes.c_char * 24),
		('result', ctypes.c_uint8)
	]


# packet 0xa13
class CZ_CHECK_RECEIVE_CHARACTER_NAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('receiveName', ctypes.c_char * 24)
	]


# packet 0xa14
class ZC_CHECK_RECEIVE_CHARACTER_NAME(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32),
		('Job', ctypes.c_uint16),
		('Clevel', ctypes.c_uint16)
	]


# packet 0xa15
class ZC_GOLDPCCAFE_POINT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('bActive', ctypes.c_uint8),
		('UnitPoint', ctypes.c_uint8),
		('Point', ctypes.c_uint32),
		('AccumulatePlaySecond', ctypes.c_uint32)
	]


# packet 0xa16
class CZ_DYNAMICNPC_CREATE_REQUEST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('NickName', ctypes.c_char * 24)
	]


# packet 0xa17
class ZC_DYNAMICNPC_CREATE_RESULT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint16)
	]


# packet 0xa18
class ZC_ACCEPT_ENTER3(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('startTime', ctypes.c_uint32),
		('PosDir', ctypes.c_char * 3),
		('xSize', ctypes.c_uint8),
		('ySize', ctypes.c_uint8),
		('font', ctypes.c_uint16),
		('sex', ctypes.c_uint8)
	]


# packet 0xa19
class CZ_REQ_OPEN_ROULETTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xa1a
class ZC_ACK_OPEN_ROULETTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('Serial', ctypes.c_uint32),
		('Step', ctypes.c_uint8),
		('Idx', ctypes.c_uint8),
		('AdditionItemID', ctypes.c_uint16),
		('GoldPoint', ctypes.c_uint32),
		('SilverPoint', ctypes.c_uint32),
		('BronzePoint', ctypes.c_uint32)
	]


# packet 0xa1b
class CZ_REQ_ROULETTE_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xa1c
class ZC_ACK_ROULEITTE_INFO(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('RouletteSerial', ctypes.c_uint32)
	]


# packet 0xa1d
class CZ_REQ_CLOSE_ROULETTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xa1e
class ZC_ACK_CLOSE_ROULETTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0xa1f
class CZ_REQ_GENERATE_ROULETTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16)
    ]


# packet 0xa20
class ZC_ACK_GENERATE_ROULETTE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('Step', ctypes.c_uint16),
		('Idx', ctypes.c_uint16),
		('AdditionItemID', ctypes.c_uint16),
		('RemainGold', ctypes.c_uint32),
		('RemainSilver', ctypes.c_uint32),
		('RemainBronze', ctypes.c_uint32)
	]


# packet 0xa21
class CZ_RECV_ROULETTE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Condition', ctypes.c_uint8)
	]


# packet 0xa22
class ZC_RECV_ROULETTE_ITEM(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8),
		('AdditionItemID', ctypes.c_uint16)
	]

class ZC_ALL_ACH_LIST_ACH(ctypes.Structure):
    _pack_ = 1
    _fields_ = [   
		('ACHID', ctypes.c_uint32),
		('bComplete', ctypes.c_uint8),
		('count1', ctypes.c_uint32),
		('count2', ctypes.c_uint32),
		('count3', ctypes.c_uint32),
		('count4', ctypes.c_uint32),
		('count5', ctypes.c_uint32),
		('completeDate', ctypes.c_uint32),
		('bGetReward', ctypes.c_uint8),
    ]
# packet 0xa23
class ZC_ALL_ACH_LIST(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('PacketLength', ctypes.c_uint16),
		('ACHCount', ctypes.c_uint32),
		('ACHPoint', ctypes.c_uint32),
        ('ACHList', ZC_ALL_ACH_LIST_ACH * 1)
    ]

# packet 0xa24
class ZC_ACH_UPDATE(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ACHPoint', ctypes.c_uint32),
		('ACHID', ctypes.c_uint32),
		('bComplete', ctypes.c_uint8),
		('count1', ctypes.c_uint32),
		('count2', ctypes.c_uint32),
		('count3', ctypes.c_uint32),
		('count4', ctypes.c_uint32),
		('count5', ctypes.c_uint32),
		('completeDate', ctypes.c_uint32),
		('bGetReward', ctypes.c_uint8)
	]


# packet 0xa25
class CZ_REQ_ACH_REWARD(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('ACHID', ctypes.c_uint32)
	]


# packet 0xa26
class ZC_REQ_ACH_REWARD_ACK(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('result', ctypes.c_uint8),
		('ACHID', ctypes.c_uint32)
	]


# packet 0xa27
class ZC_RECOVERY2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('varID', ctypes.c_uint16),
		('amount', ctypes.c_uint32)
	]


# packet 0xa28
class ZC_ACK_OPENSTORE2(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('Result', ctypes.c_uint8)
	]


# packet 0xa29
class ZC_REQ_AU_BOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]


# packet 0xa2a
class CZ_ACK_AU_BOT(ctypes.Structure):
	_pack_ = 1
	_fields_ = [
        ('packetId', ctypes.c_uint16),
		('GID', ctypes.c_uint32)
	]
