# Lab 9: Handling Waits (Implicit & Explicit)

## Objective
Learn how to handle dynamic web elements using implicit and explicit waits in Selenium.

## Tasks Completed

### Task 1: Implicit Wait
- Applied global wait of 5 seconds
- Used driver.implicitly_wait()

### Task 2: Explicit Wait
- Used WebDriverWait
- Applied expected_conditions:
  - presence_of_element_located
  - element_to_be_clickable

### Task 3: Comparison Understanding
- Implicit waits apply globally
- Explicit waits apply to specific conditions

## Concepts Used
- Selenium WebDriver
- Implicit Wait
- Explicit Wait
- WebDriverWait
- Expected Conditions (EC)

## Sample Output

Page Title: Example Domain  
Implicit Wait Element Found: Example Domain  
Explicit Wait Element Found: Example Domain  
Element is clickable (simulation)  
Test Passed Successfully!

## Files
- waits_demo.py
- README.md
