pages_count = int(input())
page_per_h = int(input())
days_to_read = int(input())
total_reading_time = float(pages_count / page_per_h)
hours_per_day = float(total_reading_time / days_to_read)
print(hours_per_day)