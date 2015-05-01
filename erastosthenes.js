/**
 * Created by yury on 29/04/15.
 */
primes_sieve = function (limit) {
    var limitn = limit + 1;
    var not_prime = []
    for(var q=0; q < limitn; q++){
        not_prime[q] = true;
    }
    not_prime[0] = false;
    not_prime[1] = false;
    var primes = [];

    for (var i = 2; i < limitn; i++) {
        if (not_prime[i]) {

            for (var j = 2; i * j < limitn; j++) {
                not_prime[i * j] = false;
            }

            primes.push(i)
        }
    }


    return primes
};

t = new Date().getTime();

primes = primes_sieve(9000000);
//console.log(primes.slice(-3));
console.log((new Date().getTime() - t) / 1000);
