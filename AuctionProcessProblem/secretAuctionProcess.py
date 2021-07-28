from auctionLogo import logo
print(logo)
bidData = {}

bid_continue = True

while bid_continue :
    name = input("What is your name---")
    bidPrice = int(input("Enter bid price---"))
    bidData[name] = bidPrice
    is_any_other_bidCandidate = input("enter (yes\no)---")
    if is_any_other_bidCandidate == "no" :
        bid_continue =  False


bidPriceList = []
for bid_candidate in bidData :
    bidPriceList.append(bidData[bid_candidate])

max_bid_price = bidPriceList[0]
for i in range(1,len(bidPriceList)) :
    if max_bid_price <bidPriceList[i] :
        max_bid_price = bidPriceList[i]

for bid_cadidate in bidData:
    if max_bid_price == bidData[bid_cadidate]:
        print(f"Bid winner is.... {bid_candidate} with {max_bid_price} price")
