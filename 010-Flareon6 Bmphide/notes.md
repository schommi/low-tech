* args[0] output file
* args[1]: other file
* args[2] output file

* Program.ctor()
  * yy = 20
  * ww = "1F7D"
  * zz = "MTgwMw=="
* Program.Init()
  * yy *= 136 => 2720
  * ww +="14" => "1F7D14"
  * for each method on A: RuntimeHelpers.PrepareMethod()
  * CalculateStack()
    * Get .NET Version
    * IdentifyLocals()
      * LoadLibrary (depends on .NET Version)
      * GetProcAddress
      * Hook?
  * ww+= "42" => "1F7D1442"
  * zz = "MzQxOTk="
  * Find 4 methods on Program by IL Hash
  * VerifySignature(m, m2)
  * VerifySignature(m3, m4)
* Program.h() : Encrypt byte array (otherfile)
* Program.i() : modify bitmap (encryptedotherfile)

*  100663317 (h)
Marshal.WriteByte((IntPtr)((void*)info->ILCode), 23, 20);
Marshal.WriteByte((IntPtr)((void*)info->ILCode), 62, 20);
=> f calls to g calls
* 100663316 (g)
Marshal.WriteInt32((IntPtr)((void*)info->ILCode), 6, 309030853);
Marshal.WriteInt32((IntPtr)((void*)info->ILCode), 18, 209897853);

VerifySignature(a, b)

Program.j(i)
* 25 => 0xfc
* 27 => 0xf8
* 100 => 6
* 103 => 0
* 228 => 7
* 230 => 3
* 231 => 1

Program.i()
* loop columns
* loop rows

```csharp
int red   = ((int)pixel.R & 0xf8) | ((int)data[num] & 7);
int green = ((int)pixel.G & 0xf8) | (data[num] >> 3) & 7);
int blue  = ((int)pixel.B & 0xfc) | (data[num] >> 6) & 3);
```

* red: lower 3 bits <= data lower 3 bits
* green: lower 3 bits <= data mid 3 bits
* blue: lower 2 bits <= data highest 2 bits


```csharp
public static byte f(int idx) // same result for same input
{
  int num = 0;
  int num2 = 0;
  byte result = 0;
  int[] array = new int[]
  {
    ...
  };
  for (int i = 0; i <= idx; i++)
  {
    num++;
    num %= 256;
    num2 += array[num];
    num2 %= 256;
    int num3 = array[num];
    array[num] = array[num2];
    array[num2] = num3;
    result = (byte)array[(array[num] + array[num2]) % 256];
  }
  return result;
}

public static byte e(byte b, byte k)
{
	for (int i = 0; i < 8; i++)
	{
		bool flag = (b >> i & 1) == (k >> i & 1);
		if (flag)
		{
			b = (byte)((int)b & ~(1 << i) & 255);
		}
		else
		{
			b = (byte)((int)b | (1 << i & 255));
		}
	}
	return b;
}

public static byte a(byte b, int r)
{
	return (byte)(((int)b + r ^ r) & 255);
}

public static byte c(byte b, int r)
{
	byte b2 = 1;
	for (int i = 0; i < 8; i++)
	{
		bool flag = (b & 1) == 1;
		if (flag)
		{
			b2 = (b2 * 2 + 1 & byte.MaxValue);
		}
		else
		{
			b2 = (b2 - 1 & byte.MaxValue);
		}
	}
	return b2;
}

public static byte[] h(byte[] data)
{
  byte[] array = new byte[data.Length]; // out len = in len
  int num = 0;
  for (int i = 0; i < data.Length; i++)
  {
    int num2 = (int)Program.f(num++); // f = same result for same input
    int num3 = (int)data[i];
    num3 = (int)Program.e((byte)num3, (byte)num2); // e = same result for same input
    num3 = (int)Program.a((byte)num3, 7); // a = same result for same input
    int num4 = (int)Program.f(num++); // f = same result for same input
    num3 = (int)Program.e((byte)num3, (byte)num4); // e = same result for same input
    num3 = (int)Program.c((byte)num3, 3); // c = same result for same input
    array[i] = (byte)num3;
  }
  return array;
}
```


* CTF: dOnT_tRu$t_vEr1fy@flare-on.com