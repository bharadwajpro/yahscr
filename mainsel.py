import sys
sys.path.append("directory where python is installed/Yahoo-Finance-Web-Scraping")

from bodysel import testforbse
from bodysel import testfornse
from bodysel import end_of_all


# Test 1 NSE
testfornse(0, 10)

# Test 2 NSE
testfornse(10, 20)

# Test 3 NSE
testfornse(20, 30)

# Test 4 NSE
testfornse(30, 40)

# Test 5 NSE
testfornse(40, 50)

# Test 6 NSE
testfornse(50, 60)

# Test 7 NSE
testfornse(60, 70)

# Test 8 NSE
testfornse(70, 80)

# Test 9 NSE
testfornse(80, 86)

# Test 10 BSE
testforbse(0, 10)

# Test 11 BSE
testforbse(10, 20)

# Test 12 BSE
testforbse(20, 30)

# Test 13 BSE
testforbse(30, 40)

# Test 14 BSE
testforbse(40, 50)

# Test 15 BSE
testforbse(50, 60)

# Test 16 BSE
testforbse(60, 70)

# Test 17 BSE
testforbse(70, 80)

# Test 18 BSE
testforbse(80, 90)

# Test 19 BSE
testforbse(90, 99)

# driver.quit()
end_of_all()

# 1st Average = 16.82 seconds
# 2nd Average = 15.01 seconds
