# Using torch.Tensor
t = torch.Tensor([[1,2,3],[3,4,5]])
print(f"Created Tensor Using torch.Tensor:\n{t}")

# Using torch.randn
t = torch.randn(3, 5)
print(f"Created Tensor Using torch.randn:\n{t}")

# using torch.[ones|zeros](*size)
t = torch.ones(3, 5)
print(f"Created Tensor Using torch.ones:\n{t}")
t = torch.zeros(3, 5)
print(f"Created Tensor Using torch.zeros:\n{t}")

# using torch.randint - a tensor of size 4,5 with entries between 0 and 10(excluded) 
t = torch.randint(low = 0,high = 10,size = (4,5))
print(f"Created Tensor Using torch.randint:\n{t}")

# Using from_numpy to convert from Numpy Array to Tensor 
a = np.array([[1,2,3],[3,4,5]])
t = torch.from_numpy(a)
print(f"Convert to Tensor From Numpy Array:\n{t}")

# Using .numpy() to convert from Tensor to Numpy array 
t = t.numpy()
print(f"Convert to Numpy Array From Tensor:\n{t}")
