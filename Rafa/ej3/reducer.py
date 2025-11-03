import sys
 
current_year=None
total_sum=0
count =0


for line in sys.stdin:
    parts = line.strip()
    parts = line.split('\t')
    year = parts[0]
    price = float(parts[1])
    count = int(parts[2])
    
    if year == current_year:
        total_sum += price
        count += 1
    else:
        if current_year is not None:
                average_price = sum_prices / count_records
                print(f"{current_year}\t{average_price:.2f}")
            
            # Reiniciar acumuladores para el nuevo año
        current_year = year
        sum_prices = price
        count_records = count
