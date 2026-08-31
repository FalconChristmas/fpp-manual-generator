# Creating a Proxy Host {#creating-a-proxy-host}

You can use an FPP device to route network traffic between subnets by setting
it up as a **Proxy Host**, instead of configuring a
[static route](#configuring-a-static-route). This is especially useful when
you cannot add a static route to your router and are using a Mac (since Macs
do not support persistent routes) — though a Proxy Host works just as well
with Windows computers.

Open **Status/Control → Proxy Settings** and enter the IP address of the
controller(s) attached to the FPP device. To reach a proxied controller's web
UI afterwards, click its link on the Proxied Hosts list, or browse to the FPP
device's IP followed by `/proxy/` and the controller's address — for example
`192.168.1.101/proxy/192.168.101.2`.

See [Proxy Settings](#proxy-settings) for the full page reference, including
how to configure proxies directly from xLights via **FPP Connect**.
