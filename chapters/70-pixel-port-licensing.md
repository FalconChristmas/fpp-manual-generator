# Pixel Port Licensing

Two pixel‑output protocols need a licence to use their advanced features:
**DPIPixels** and **BBBStrings48**. No other use of FPP requires a licence. The
advanced features are **more than 50 pixels per port** and support for **remote
receivers**.

> **Note:** If you are not using these protocols, or do not need their advanced
> functionality, you do **not** need a licence. There is a licensing FAQ at
> `https://shop.falconplayer.com/faqs/`.

## Do I need a licence?

### Raspberry Pi based controllers

- Using a Pi hat for **up to 3 ports** (or pixels straight on the GPIO pins) with
  the **PiHat** protocol — **no licence**. (This uses the Pi's PWM, so on‑board
  audio is unavailable; use a USB audio adapter such as the SoundBlaster Play 3 —
  a very common setup.)
- Using a hat that drives **more than 3 ports**, or wanting on‑board audio with a
  2‑port hat — **licence required**, *unless* you use **50 pixels or fewer per
  port**.

### BeagleBone based controllers

- **50 pixels or fewer per port** — no licence (but Differential Remotes cannot be
  used without one).
- **More than 50 pixels on any port**, or using remote receivers — **licence
  required**.

## Getting a licence

The vendor you bought your controller from may have supplied a **voucher** — if so,
see *Redeeming a Voucher* below. Otherwise decide how many ports you need, go to
`https://shop.falconplayer.com/`, choose the key for that number of ports, and add
it to your cart (the *How To Guides* at the top of the shop are helpful; click a
key for more detail).

> **Note:** For a **DIY board**, choose the appropriate key and enter the relevant
> **coupon code** at checkout to get the licence for free.

### Purchasing a licence

Add the licence to your cart and pay with PayPal/Venmo, or **Proceed to
checkout** for other methods. On completion you receive an **Order Number** and
**License Key** on the confirmation page and by email. You can then sign your
EEPROM as below.

## Applying a licence key

There are two ways to apply a licence:

- **On‑Line Signing** – easiest; use it if your FPP has internet access.
- **Off‑Line Signing** – a few more steps, for when the FPP network has no
  internet (temporarily connecting the FPP to the internet just to sign may be
  easier).

### On‑Line Signing

1. Open **Input/Output Setup → Channel Outputs → Pixel Strings**. If no cape is
   detected, install the correct **Virtual EEPROM** first (see *Channel Outputs →
   Configuring the Virtual EEPROM*).
2. Click the **Cape Info** link in the blue banner.
3. On the Cape Info page, open the **EEPROM Signature** tab.
4. Enter your **Order Number** and **License Key** and click **Sign EEPROM**.
5. When it shows *Signing Complete. Please Reboot*, click **Close**, then
   **Reboot** and confirm.

Once signed, the Pixel Strings tab shows the cape type as its name and the blue
banner disappears.

### Off‑Line Signing

1. As above, open **Channel Outputs → Pixel Strings** (installing the Virtual
   EEPROM if needed) and click the **Cape Info** link.
2. Open the **Offline Signing** tab, enter your **Order Number** and **License
   Key**, and click **Download Offline Signing Packet**. The downloaded file's name
   includes the device's host name — so keep host names unique to match the right
   file to the right device.
3. Move that file to a computer with internet access (physically move the computer,
   or copy via USB), go to
   `https://shop.falconplayer.com/offline-signing/`, enter the same Order Number
   and License Key, select the signing file, and click **Sign**. A **signed**
   EEPROM file is downloaded.
4. Bring the signed file back to the computer connected to the FPP, return to
   **Cape Info → Offline Signing**, choose the signed file (its name contains
   *signed* and the host name), and click **Upload Signed Packet**.

After a few seconds it shows your EEPROM signature details.

## Redeeming a voucher

A vendor may supply a voucher when you buy a controller (this does **not** apply to
Falcon or KulpLights controllers, which are pre‑signed). There are two ways to
redeem it:

- **FPP Redemption** *(easiest, needs internet on the FPP)* – get the licence and
  sign the EEPROM directly from the FPP interface: go to **Help → Cape Info**, open
  the **Voucher Redemption** tab, fill in the details, and click **Redeem
  Voucher**.
- **shop.falcon Redemption** – log in at `https://shop.falconplayer.com/`, redeem
  the voucher there to get your key, then apply the key on your FPP device as in
  *Applying a Licence Key*.

> **Screenshots pending — cape hardware required.** The signing screens appear on
> the Cape Info and Pixel Strings pages, which need a cape/Virtual EEPROM present;
> these will be captured on a cape‑enabled system.
