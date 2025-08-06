#include<bits/stdc++.h>
using namespace std;
#define int long long
struct flower{
    string name;
    int id,a;
}a[1010];
vector<string> ans;
int sum=0;
bool cmp(flower x,flower y){
    if(x.a!=y.a)return x.a<y.a;
    return x.id<y.id;
}
signed main(){
    int n,m,k;
    cin>>n>>m>>k;
    for(int i=1;i<=n;i++)cin>>a[i].name;
    for(int i=1;i<=n;i++)cin>>a[i].a,a[i].id=i;
    sort(a+1,a+n+1,cmp);
    for(int i=1;i<=m;i++){
        sum+=a[i].a;
        if(sum>k){
            cout<<"No Mark";
            return 0;
        }
        ans.push_back(a[i].name);
    }
    cout<<sum<<endl;
    for(int i=0;i<ans.size();i++)cout<<ans[i]<<" ";
    return 0;
}