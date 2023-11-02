Errors are of two types 
1) syntax errors - no way to handle syntax errors
2) Runtime errors(exceptions) - these occurs during only runtime, there is way to handle runtime errors/exceptions

when we need to use exception handling in pyhton script - Assume that there is a script, and if there is any chance to get any runtime error we need to handle it

try:
    actual code, we need to write in this block, if something goes wrong with any of the statement in try block, then python automatically skip the try block and executes the except block, if any statement in try block gets interrupted, the following statement won't gonna execute
except Exception as e:
    print(e)
else:
    else is optional, this is gonna execute if there are no exceptions in try block

finally:
        finally is optional, irrespective of two blocks try and except this gonna execute

Exception handling for known exceptions - known exception means suppose, if we're able to predict exceptions what the exception we gonna get for the code in this we need of use except Exception as e, directly we can handle it


creating custom exceptions - we can create custom exceptions using
raise - (used to raise an existing exceptions)
assert - (used to create and AssertionError), it gonna raise the AssertionError exception when a condition is false






