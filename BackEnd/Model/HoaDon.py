from pydantic import BaseModel
from typing import Union
from datetime import date



class HoaDonBanHang(BaseModel):
    id: int
    phap_nhan_mua_hang: Union[str, None] = None
    ngay_mua: Union[date, None] = None
    danh_sach_hang_mua: Union[list, None] = None

class HoaDonMuaHang(BaseModel):
    id: int
    phap_nhan_ban_hang: Union[str, None] = None
    ngay_ban: Union[date, None] = None
    danh_sach_hang_ban: Union[list, None] = None