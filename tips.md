## Network Issue

+ Issue: fatal: unable to access 'https://github.com/\<username>/\<repositoryname>.git/': Failed to connect to github.com port 443 after 21110 ms: Could not connect to server

> Solution:
>
> ```powershell
> >>>git config --global http.proxy 127.0.0.1:7890
> 
> >>>git config --global https.proxy 127.0.0.1:7890
> ```
>
> Way to reset:
>
> ```powershell
> >>>git config --global --unset http.proxy
> >>>git config --global --unset https.proxy
> ```
>
> 