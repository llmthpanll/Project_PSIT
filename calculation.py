#cost ราคาขาย, amount จำนวนที่ขาย, stock ของใน stock, shop ราคาสั่งซื้อ
"""calculation"""
def income(cost, amount):
    """"รายรับของร้าน"""
    return  cost*amount
def buy(stock, shop):
    """"ราคาสินค้าทีสั่งเพิ่มต่อวัน"""
    return stock-shop
