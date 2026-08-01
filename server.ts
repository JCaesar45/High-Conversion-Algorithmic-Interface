// Overload signatures to preserve type safety across all cases
function deprecatedWrapper<T extends (...args: any[]) => any>(oldFn: T, newFn: T): T;
function deprecatedWrapper<U extends any[], V>(oldFn: (...args: U) => V, newFn: (...args: U) => V): (...args: U) => V;

// Single implementation handling all cases, delegating to the new API
function deprecatedWrapper(oldFn: (...args: any[]) => any, newFn: (...args: any[]) => any): (...args: any[]) => any {
    return ((...args: Parameters<typeof oldFn>): ReturnType<typeof oldFn> => {
        console.warn('Deprecated, use newFn instead.');
        return newFn(...args);
    }) as any;
}

// Example usage demonstrating type safety
function newApiCall(id: number, name: string): boolean {
    return true;
}

const safeLegacyWrapper = deprecatedWrapper(
    function oldApiCall(id: number, name: string): boolean { return false; },
    newApiCall
);

// TypeScript will enforce that safeLegacyWrapper accepts (number, string) and returns boolean
