






"""
highest price wins for buy
lowest price wins for sell

first one in gets higher priority


"""



from dataclasses import dataclass

@dataclass()
class Order:
    type: int # buy =0, sell=1
    price: int
    quantity: int
    timestamp: int
    id: int
    active: bool



class TradeRecord:
    buy_order_id: int
    sell_order_id: int
    execution_price: int
    executed_qty: int


import heapq



from typing import Any
class OrderBook:
    def __init__(self):
        self.buys = [] # highest first (maxheap), (-price, time, order)
        self.sells = [] # lowest first (price, time, order ) minheap

        self.orders = {} # order id to order
        self.tick = 0
        self.nextid = 1

    def place_order(self, side: int, price: int, qty: int):
        # return list of trade recs
        t = self.tick
        self.tick +=  1

        curr_id =  self.nextid

        self.nextid += 1

        order = Order(type=side, price=price, timestamp=t, quantity=qty, id = curr_id, active=True)
        
        self.orders[curr_id] = order

        if side == "buy":
            heapq.heappush(self.buys, (-price, t, order))
        elif side == "sell":
            heapq.heappush(self.sells, (price, t, order))

        
        self._run_match(type=side)

        return curr_id



    def cancel(self, order_id):
        o: Order | None = self.orders.get(order_id, None)
        if not o or not o.active:
            return False
        
        o.active = False
        o.quantity = 0

        return True
        
    def _run_match(self, type: int):
        while True:
            best_buy = self._best_buy()
            best_sell = self._best_sell()
            
            if not best_buy or not best_sell:
                return 

            buyprice, buy_order = best_buy
            sellprice, sell_order = best_sell

            if sellprice > buyprice: 
                return # no buyer would buy that

            market_price = 0
            if type == "buy":
                market_price = sellprice
            elif type == "sell":
                market_price = buyprice

            # whateve ris avialable has to be the min
            qty = min(buy_order.quantity, sell_order.quantity)

            buy_order.quantity -= qty
            sell_order.quantity -= qty

            print(f"done trade {qty} at {market_price}")

            if buy_order.quantity == 0:
                # exhausted all?
                buy_order.active = False
                heapq.heappop(self.buys)
            elif sell_order.quantity == 0:
                sell_order.active = False
                heapq.heappop(self.sells)



    def _remove_stale(self, heap):
        # remove stale canceled at the top
        while heap and not heap[0][2].active:
            heapq.heappop(heap)


    def _best_buy(self):
        self._remove_stale(self.buys)
        if not self.buys:
            return None # nobody buying

        price, _, o = self.buys[0]
        return -price, o # return price and order

    def _best_sell(self):
        self._remove_stale(self.sells)
        if not self.sells: return None
        
        price, _, o = self.sells[0]
        return price, o


















