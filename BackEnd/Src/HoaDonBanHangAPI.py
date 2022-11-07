from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from Model.HoaDon import HoaDonBanHang
from SupportModule.jsonFile import *

data_dir = "./Data/HoaDonBanHang.json"
arr_Items = read_json_data(data_dir)

router = APIRouter(
    prefix="/HoaDonBanHang",
    tags=["HoaDonBanHang"],
    responses={404: {"description": "Not found"}},
)



@router.get("/")
async def read_item():
    return {"Items":arr_Items}

@router.put("/")
# Do các attribute đã là optional nên cần thêm điều kiện require khi tạo mới
async def add_new_item(item: HoaDonBanHang):
    item.id = len(arr_Items)
    arr_Items.append(item)
    write_json_data(data_dir, [x.__dict__ for x in arr_Items])
    return {"item_id": item.id, "Item": item}

@router.get("/HoaDonBanHangByID/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    try:
        return {"item":arr_Items[item_id], "q": q}
    except:
        raise HTTPException(status_code=404, detail="Item not found")

@router.patch("/HoaDonBanHangByID/")
async def update_item_patchial(item: HoaDonBanHang):
    item_id = item.id
    if item_id > len(arr_Items):
        raise HTTPException(status_code=404, detail="Item not found")
    arr_Items[item_id].update(item.dict(exclude_unset=True))
    write_json_data(data_dir, [x for x in arr_Items])
    return arr_Items[item_id]

# https://fastapi.tiangolo.com/tutorial/bigger-applications/