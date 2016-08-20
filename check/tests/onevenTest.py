import test as t
import lib
import assertlib

@t.test(0)
def exact(test):
    def testMethod(fileName):
        result = lib.outputOf(fileName)
        testResult = assertlib.exact(result.strip(), "100")
        return testResult, result
    test.test = testMethod
    
    test.description = lambda : "output is exactly 100"
    test.fail = lambda info : "expected: 100, but got \"%s\" instead" %info

@t.failed(exact)
@t.test(1)
def contains(test):
    def testMethod(fileName):
        result = lib.outputOf(fileName)
        testResult = assertlib.contains(result, "100")
        return testResult, result
    test.test = testMethod
    
    test.description = lambda : "contains 100 in the output"
    test.success = lambda info : "the correct answer (100) can be found in the output"
    test.fail = lambda info : "the correct answer (100) cannot be found in the output"