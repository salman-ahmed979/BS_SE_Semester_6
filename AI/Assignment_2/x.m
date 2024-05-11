#include <Foundation/Foundation.h>

int main(int argc, const char * atgv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSLog (@"Hello World");
    [pool drain];
    return 0;
}