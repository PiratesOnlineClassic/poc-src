# Window:
window-title Pirates Online Classic
icon-filename phase_3/etc/Pirates_Adds.ico
win-size 800 600
fullscreen #f

# Dev:
want-dev #f

# Display:
load-display pandagl
aux-display pandadx9
aux-display pandadx8
aux-display p3tinydisplay

# Audio:
audio-music-active #t
audio-library-name p3fmod_audio
audio-output-rate 44100

# Models:
want-disk-cache #t
default-model-extension .bam

# Exclude:
exclude-texture-scale BardiT*
exclude-texture-scale BriosoPro*
exclude-texture-scale Buccaneer_outline_1*
exclude-texture-scale playingcards*
exclude-texture-scale gui_*
exclude-texture-scale loading_screen*
exclude-texture-scale loadingscreen_*
exclude-texture-scale loading_window_texture*
exclude-texture-scale vr_*
exclude-texture-scale general_frame_*
exclude-texture-scale drop-shadow

# Stencil:
stencil-bits 8

# DClass:
dc-file astron/dclass/pirates.dc
dc-file astron/dclass/otp.dc

# Server:
server-port 6667
server-version pirates-dev
want-ssl-scheme 0
game-server 127.0.0.1
want-user-funnel #f

# Notifier:
notify-level-tiff error
notify-level-dxgsg warning
notify-level-gobj warning
notify-level-loader warning
notify-level-chan fatal
notify-level-pgraph error
notify-level-collide error
notify-level-abs error
notify-level-Actor error
notify-level-DisplayOptions debug
notify-level-express error
notify-timestamp 1

# Buffer:
framebuffer-hardware #t
framebuffer-software #f
framebuffer-alpha 1
alpha-bits 8
prefer-parasite-buffer 1
force-parasite-buffer 1
hardware-animated-vertices #t
textures-auto-power-2 #t
framebuffer-multisample 1
multisamples 2

# Performance:
lock-to-one-cpu #f
lock-to-one-core #f

# Tutorial:
skip-tutorial #f
force-tutorial #t
force-tutorial-complete #f

# Seapatch:
want-seapatch #t

# Special Effects:
want-special-effects #t

# Make A Pirate:
want-make-a-pirate #t
want-new-avatars #t
want-avatar-shadows #t
want-new-avatar #t
want-npc-viewer #f

# Membership:
want-membership #t

# Islands:
want-island-barriers #t
object-load-delay #f

# Motion:
motionfsm-lag #t
avatar-physics-freq 2.0
npc-sidestep #f

# Smoothing:
smooth-lag 1
smooth-prediction-lag 1

# Analytics:
analytics-game-key 5de6a7ce0decbe613cf1cd172b319faf
analytics-secret-key eb6753270d979378bb301d4b82f27a36d1bcc3bb
want-analytics #t

# Discord:
discord-client-id 442413702428229632
discord-rpc-version 1
want-discord-rich-presence #t
discord-want-elapsed #t
discord-development-message #f
allow-teleport-from-discord #f

# Alpha:
want-alpha-blockers #f

# Quests:
disable-blockers #f

# Text:
want-render2dp 1
text-encoding utf8
direct-wtext 0
text-never-break-before ,.-:?!;
textures-power-2 down

# Clock:
async-request-timeout 80.0
async-request-break-on-timeout 0
clock-mode limited
clock-frame-rate 120
paranoid-clock 1
ime-aware 1
ime-hide 1

# TCP/SSL:
collect-tcp 1
collect-tcp-interval 0.1
verify-ssl 0

# Lod:
default-lod-type fade
lod-fade-time 2
make-grid-lod 1
verify-lods 0

# Texture:
dx-management 0
dx-texture-management 0
retransform-sprites 1
preload-textures 0
allow-incomplete-render 1

# Misc:
want-tattoos 1
want-jewelry 1
want-emotes 1
want-slash-commands 1
want-magic-words 1
want-map-flavor-anims 1
low-weapons-only 1
want-running 0
enforce-clean-exit 1
want-ships 1
game-phase 1

# Game Options:
want-game-options-hdr 0
want-game-options-ship-visibility 1
want-cpu-frequency-warning #f

# Cache:
model-cache-max-kbytes 262144
launcher-decompress-buffer-size 65536

# Pvp:
want-privateering 1
want-infamy 0

# Options:
ocean-visibility 1

# Other:
test-saint-patricks-day #f
test-fourth-of-july #f
want-enviro-dr #f
