# Medir Tempo de Ordenação


## Java

```java
    long tempoInicio, tempoFim;

    tempoInicio = System.nanoTime();
    // rotina1
    tempoFim = System.nanoTime();
    System.out.println("Tempo (ms) rotina 1: " + (tempoFim - tempoInicio)/1000000);

    tempoInicio = System.nanoTime();
    // rotina2
    tempoFim = System.nanoTime();
    System.out.println("Tempo (ms) rotina 2: " + (tempoFim - tempoInicio)/1000000);
```

## Python
```python
    tempoInicio = time.time()
    # rotina 1
    tempoFim = time.time()
    print("Tempo da rotina 1: ", (tempoFim - tempoInicio) , "s")
```


