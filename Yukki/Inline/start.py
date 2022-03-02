from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Ses Kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Ses Düzeyi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Yetkili Kullanıcılar", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Tablo", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Kapat", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Ayarlar**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Ayarlar", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Ayarlar", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Destek Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Ayarlar", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨 Destek Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Beni Grubuna Ekle ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Beni Grubuna Ekle ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Destek Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Beni Grubuna Ekle ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Yardımcı Komutlar Menüsü",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Beni Grubuna Ekle ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Resmi Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨 Destek Grubu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Bu {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Ses Kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Ses Düzeyi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Yetkili Kullanıcılar", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Tablo", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Kapat", callback_data="close"),
            InlineKeyboardButton(text="🔙 Geri Git", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Ayarlar**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Ses Düzeylerini Sıfırla 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Alçak Ses", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Orta Ses", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Yüksek Ses", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Güçlendirilmiş Ses", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Özel Birim 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri Git", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Ayarlar**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 Özel Birim 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Ayarlar**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Herkes", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Yöneticiler", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Yetkili Kullanıcı Listeleri", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri Git", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Ayarlar**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Geri Git", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons
