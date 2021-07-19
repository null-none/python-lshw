# lshw
lshw is a small tool to extract detailed information on the hardware configuration of the machine.

### Pip install

```bash
pip install lshw
```

### Example


```python

from lshw.client import ListHardware

list_hardware = ListHardware()
result = list_hardware.read_data(list_hardware.get_nic_data())
print(result)
```

### License

MIT