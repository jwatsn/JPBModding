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
- In the root of the Content folder, right click the "Generate Pak" Editor utility widget and click "Run Editor Utility Widget"<br><br>
<img width="283" height="803" alt="image" src="https://github.com/user-attachments/assets/af5910bc-25e1-4e75-8945-98e7127d9c34" /><br><br>
- Optionally choose a name and a chunk id. Chunk ID's only matter if you plan on using multiple asset paks together. They also need to be a positive number. Leave the default if unsure.
- Click "Create Pak" and once it's done, it will create a .pak file in the PakOutput folder within the project root dir<br><br>
<img width="232" height="159" alt="image" src="https://github.com/user-attachments/assets/27665d3a-3b65-4b13-9571-7f1ce6af0655" /><br><br>

- Browse to "C:\Program Files (x86)\Steam\steamapps\common\Jetpack Battle Playtest\JPB" (Location might differ if your steam installs games somewhere else or is installed somewhere else)<br><br>

- Create a folder called "Paks" if it doesn't exist.<br><br>
<img width="618" height="475" alt="image" src="https://github.com/user-attachments/assets/243a4c3f-a5ec-4c38-b9fd-f06b98df5126" /><br><br>
- Move the new pak file into the Paks folder <br><br>
- Launch Jetpack Battle<br><br>
- You can now use the custom static mesh as an "InteriorShape" by placing it through the JPB Editor<br><br>
<img width="340" height="215" alt="image" src="https://github.com/user-attachments/assets/8a7fe8cd-5c4a-4cf4-b72b-f968f9c3448f" /><br><br>
<img width="1602" height="932" alt="image" src="https://github.com/user-attachments/assets/b20ae004-0b62-4268-bc10-4efdb02fa68b" />








