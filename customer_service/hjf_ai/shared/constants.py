# -*- coding: utf-8 -*-
"""
constants - 全局常量定义

定义系统中使用的所有常量，包括：
- 默认路径和端口
- 降级原因常量
- 命令和模式名称
- 槽位类型
"""

from typing import Final


# =============================================================================
# 默认路径
# =============================================================================

DEFAULT_DOMAIN_PATH: Final[str] = "domain.yml"
"""默认Domain文件路径"""




# =============================================================================
# 槽位类型常量
# =============================================================================
SLOT_TYPE_TEXT: Final[str] = "text"
"""文本槽位类型"""

SLOT_TYPE_BOOL: Final[str] = "bool"
"""布尔槽位类型"""

SLOT_TYPE_FLOAT: Final[str] = "float"
"""浮点槽位类型"""

SLOT_TYPE_LIST: Final[str] = "list"
"""列表槽位类型"""

SLOT_TYPE_ANY: Final[str] = "any"
"""任意类型槽位"""

SLOT_TYPE_CATEGORICAL: Final[str] = "categorical"
"""分类槽位类型"""









# =============================================================================
# Action名称常量
# =============================================================================

ACTION_LISTEN: Final[str] = "action_listen"
"""监听用户输入动作"""

ACTION_RESTART: Final[str] = "action_restart"
"""重启会话动作"""

ACTION_SESSION_START: Final[str] = "action_session_start"
"""会话开始动作"""

ACTION_DEFAULT_FALLBACK: Final[str] = "action_default_fallback"
"""默认降级动作"""

ACTION_DEACTIVATE_LOOP: Final[str] = "action_deactivate_loop"
"""停用循环动作"""

ACTION_BACK: Final[str] = "action_back"
"""返回上一步动作"""



# =============================================================================
# 其他常量
# =============================================================================

DEFAULT_SENDER_ID: Final[str] = "default"
"""默认发送者ID"""

DEFAULT_ENCODING: Final[str] = "utf-8"
"""默认文件编码"""