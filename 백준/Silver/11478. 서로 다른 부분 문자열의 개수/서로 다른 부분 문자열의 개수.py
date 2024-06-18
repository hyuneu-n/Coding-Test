S = input()
st = set()
for i in range(len(S)):
    for sub in range(i, len(S)):
        st.add(S[i:sub+1])
print(len(st))