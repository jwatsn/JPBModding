# JPBModding
A template project for Unreal Engine to package assets for Jetpack Battle modding


<hr></hr>
<h1>How to use:</h1>
- Open up the project in Unreal engine<br><br>
- In the content folder, open up the Mods folder<br><br>
<img width="583" height="215" alt="image" src="https://github.com/user-attachments/assets/d50815de-0181-4fed-94d6-bf5d2b450ce6" />
<br>(Ignore ModAssetLabel and the Mod blueprint. Those dont need to be touched.)<br><br>
- Rename the "RenameMe" folder to something that makes sense for the mod (Or doesn't)<br>
<img width="126" height="184" alt="image" src="https://github.com/user-attachments/assets/dc83b74d-69d6-491d-8301-23d5dee14ce7" /> <img width="126" height="184" alt="image" src="https://github.com/user-attachments/assets/afa49ee0-acfe-4c08-9399-18fa464d183c" />
<br><br>
- Click the import button to import a static mesh model<br>
<img width="88" height="28" alt="image" src="https://github.com/user-attachments/assets/535dca7d-5983-4755-b0b5-cdc79bfb5f94" />
<br><br>
- In the import dialog, make sure "Build Nanite" is turned off<br>
<img width="396" height="222" alt="image" src="https://github.com/user-attachments/assets/47da796b-f08a-40c3-9faf-9b7ba27b995f" /><br><br>
<img width="851" height="309" alt="image" src="https://github.com/user-attachments/assets/a35e3e86-6712-4bae-88db-0882641ffcc8" /><br><br>
- At the top of the editor, click "Package Project"<br>
<img width="493" height="624" alt="image" src="https://github.com/user-attachments/assets/253c2154-220a-4e71-a5d1-499199e61efe" /><br>
(If the "Package Project" option is greyed out, click on the "Windows" option under package for, just below "Package Project")<br>
<img width="237" height="22" alt="image" src="https://github.com/user-attachments/assets/9be1b053-1dc9-4d64-ae32-a441d08b2d5b" /><br><br>
- Select any folder you want to package into. The first packaging can take a bit, due to Unreal Engine cooking a bunch of unneeded stuff. After the first packaging, all subsequent packaging will go MUCH faster.
<br><br>
- Once packaging is done, browse to PackageOutputFolder\Window\JPB\Content\Paks<br><br>
- You should see 2 pak files. pakchunk0-Windows.pak and pakchunk99-Windows.pak<br><br>
<img width="634" height="65" alt="image" src="https://github.com/user-attachments/assets/dfed4ca3-4c8a-4111-a791-d2d2106eff1b" /><br><br>

- pakchunk99-Windows.pak is the pakfile with custom assets you use for Jetpack Battle.<br><br>
- You can rename the Windows portion of the pak filename, but the beginning MUST start with pakchunk99- due to Unreal Engine stuff.<br><br>

- Browse to "C:\Program Files (x86)\Steam\steamapps\common\Jetpack Battle Playtest\JPB" (Location might differ if your steam installs games somewhere else or is installed somewhere else)<br><br>

- Create a folder called "Paks" if it doesn't exist.<br><br>
<img width="618" height="475" alt="image" src="https://github.com/user-attachments/assets/243a4c3f-a5ec-4c38-b9fd-f06b98df5126" /><br><br>
- Move the pakchunk99 pak file into the Paks folder <br><br>
- Launch Jetpack Battle<br><br>
- You can now use the custom static mesh as an "InteriorShape" by placing it through the JPB Editor<br><br>
<img width="340" height="215" alt="image" src="https://github.com/user-attachments/assets/8a7fe8cd-5c4a-4cf4-b72b-f968f9c3448f" /><br><br>
<img width="1602" height="932" alt="image" src="https://github.com/user-attachments/assets/b20ae004-0b62-4268-bc10-4efdb02fa68b" />






